const fs = require('node:fs');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const source = fs.readFileSync(__dirname + '/../dist/app.js','utf8');

function setup({api=true, standalone=false}={}) {
  const timers = new Map();
  let timerID = 0;
  class Element {
    constructor() { this.handlers={}; this.children=[]; this.dataset={}; this.hidden=false; this.textContent=''; }
    addEventListener(name, callback) { (this.handlers[name] ??= []).push(callback); }
    emit(name, event={}) { for (const callback of this.handlers[name] ?? []) callback(event); }
    replaceChildren(...children) { this.children=children; }
    showModal() { this.open=true; }
    close() { this.open=false; this.emit('close'); }
    focus() { this.focused=true; }
    remove() { this.removed=true; }
  }
  const selectors = ['#trailer-dialog','#trailer-frame','#trailer-poster','#trailer-poster-image',
    '#trailer-status','#retry-trailer','#close-trailer-dialog','#trailer-dialog-title',
    '#trailer-poster-title','#trailer-publisher','#trailer-external'];
  const nodes=Object.fromEntries(selectors.map(s=>[s,new Element()]));
  const link = new Element();
  link.dataset={trailerId:'FZQvIJxG9Xs',trailerTitle:'The Shining',trailerPublisher:'Warner Bros. Entertainment',trailerThumbnail:'https://i.ytimg.com/vi/FZQvIJxG9Xs/hqdefault.jpg'};
  link.href='https://www.youtube.com/watch?v=FZQvIJxG9Xs';
  let controls;
  let destroyed=0;
  const window = api ? {YT:{Player:class {
    constructor(frame, options) { controls=options.events; }
    destroy() { destroyed++; }
  }}} : {};
  const document={
    documentElement:{classList:{add(){}},hasAttribute(){return standalone;}},
    querySelector:s=>nodes[s] ?? null,
    querySelectorAll:s=>s==='[data-trailer-id]' ? [link] : [],
    addEventListener(){},
    createElement:()=>new Element(),
    head:{append(script){document.script=script;}}
  };
  vm.runInNewContext(source,{document,window,location:{protocol:'https:',origin:'https://example.com'},
    URLSearchParams,Promise,Error,setTimeout:(fn,ms)=>{timers.set(++timerID,{fn,ms});return timerID;},clearTimeout:id=>timers.delete(id)});
  return {nodes,link,document,window,get controls(){return controls;},get destroyed(){return destroyed;},
    click() { const event={button:0,preventDefault(){this.prevented=true;}};link.emit('click',event);return event; },
    runTimer(ms){const entry=[...timers].find(([,timer])=>timer.ms===ms);assert(entry);timers.delete(entry[0]);entry[1].fn();}};
}
const tick=async()=>{await Promise.resolve();await Promise.resolve();};

(async()=>{
  const failure=setup();
  assert(failure.click().prevented);
  await tick();
  failure.controls.onReady();
  failure.controls.onError({data:153});
  assert.equal(failure.nodes['#trailer-frame'].children.length,0);
  assert.equal(failure.nodes['#trailer-poster'].hidden,false);
  assert.equal(failure.nodes['#retry-trailer'].hidden,false);
  assert.match(failure.nodes['#trailer-status'].textContent,/Se på YouTube/);
  assert.equal(failure.nodes['#trailer-external'].href,failure.link.href);
  assert.equal(failure.destroyed,1);

  const missingScript=setup({api:false});
  missingScript.click();
  missingScript.document.script.onerror();
  await tick();
  assert.match(missingScript.nodes['#trailer-status'].textContent,/Forbindelsen/);
  assert.equal(missingScript.nodes['#trailer-frame'].children.length,0);

  const loading=setup(); loading.click(); await tick(); loading.runTimer(12000);
  assert.equal(loading.nodes['#trailer-poster'].hidden,false);
  assert.match(loading.nodes['#trailer-status'].textContent,/ikke indlæses/);

  const buffering=setup();buffering.click();await tick();buffering.controls.onReady();buffering.runTimer(18000);
  assert.match(buffering.nodes['#trailer-status'].textContent,/ikke starte/);
  assert.equal(buffering.nodes['#trailer-frame'].children.length,0);

  const closed=setup({api:false});closed.click();closed.nodes['#trailer-dialog'].close();
  closed.window.YT={Player:class {constructor(){throw new Error('Must not create player after closing');}}};
  closed.window.onYouTubeIframeAPIReady();await tick();
  assert.equal(closed.nodes['#trailer-frame'].children.length,0);
  assert(closed.link.focused);

  const local=setup({standalone:true});assert.equal(local.click().prevented,undefined);
  console.log('PASS: provider error 153, script failure, readiness timeout, playback timeout, close race, standalone links.');
})().catch(error=>{console.error(error);process.exitCode=1;});
