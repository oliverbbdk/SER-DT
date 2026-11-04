document.documentElement.classList.add('js-ready');

const menuButton = document.querySelector('.menu-toggle');
const menu = document.querySelector('.nav-links');
menuButton?.addEventListener('click', () => {
  const expanded = menuButton.getAttribute('aria-expanded') === 'true';
  menuButton.setAttribute('aria-expanded', String(!expanded));
  menu.classList.toggle('open', !expanded);
});
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && menu?.classList.contains('open')) {
    menu.classList.remove('open');
    menuButton.setAttribute('aria-expanded', 'false');
    menuButton.focus();
  }
});

const dayButtons = [...document.querySelectorAll('[data-day-button]')];
function selectDay(day) {
  dayButtons.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.dayButton === day)));
  document.querySelectorAll('[data-day-program]').forEach(program => {
    program.hidden = program.dataset.dayProgram !== day;
  });
}
if (dayButtons.length) {
  const requestedDay = new URLSearchParams(location.search).get('dag');
  selectDay(requestedDay === 'lordag' ? 'lordag' : 'fredag');
  dayButtons.forEach(button => button.addEventListener('click', () => {
    selectDay(button.dataset.dayButton);
    const address = new URL(location.href);
    address.searchParams.set('dag', button.dataset.dayButton);
    history.replaceState({}, '', address);
  }));
}

const comparison = document.querySelector('#comparison-position');
const stage = document.querySelector('.compare-stage');
comparison?.addEventListener('input', () => {
  stage.style.setProperty('--position', `${comparison.value}%`);
  comparison.setAttribute('aria-valuetext', `${comparison.value} procent original illustration`);
});

const ticketForm = document.querySelector('#ticket-form');
if (ticketForm) {
  const quantity = ticketForm.querySelector('#quantity');
  const total = document.querySelector('#order-total');
  const selectedText = document.querySelector('#selected-ticket');
  const dialog = document.querySelector('#ticket-dialog');
  const formatPrice = amount => new Intl.NumberFormat('da-DK', {
    style: 'currency', currency: 'DKK', maximumFractionDigits: 0
  }).format(amount);
  function updateOrder() {
    const selected = ticketForm.querySelector('input[name="ticket"]:checked');
    ticketForm.querySelectorAll('.ticket-option').forEach(card => {
      card.classList.toggle('selected', card.contains(selected));
    });
    const count = Number(quantity.value);
    total.textContent = formatPrice(Number(selected.value) * count);
    selectedText.textContent = `${count} × ${selected.dataset.name}`;
    return { selected, count, price: Number(selected.value) * count };
  }
  ticketForm.addEventListener('change', updateOrder);
  ticketForm.addEventListener('submit', event => {
    event.preventDefault();
    const { selected, count, price } = updateOrder();
    document.querySelector('#demo-selection').textContent = `${count} × ${selected.dataset.name} — ${formatPrice(price)}`;
    dialog.showModal();
  });
  document.querySelector('#close-ticket-dialog').addEventListener('click', () => dialog.close());
  dialog.addEventListener('click', event => { if (event.target === dialog) dialog.close(); });
  updateOrder();
}

const trailerDialog = document.querySelector('#trailer-dialog');
// Keep real YouTube links usable without JavaScript and in the downloadable file.
if (trailerDialog && location.protocol !== 'file:' && !document.documentElement.hasAttribute('data-standalone')) {
  const frameHost = document.querySelector('#trailer-frame');
  const poster = document.querySelector('#trailer-poster');
  const posterImage = document.querySelector('#trailer-poster-image');
  const status = document.querySelector('#trailer-status');
  const retry = document.querySelector('#retry-trailer');
  let apiPromise;
  let player;
  let currentLink;
  let attempt = 0;
  let readyTimeout;
  let playbackTimeout;

  function loadYouTube() {
    if (window.YT?.Player) return Promise.resolve(window.YT);
    if (apiPromise) return apiPromise;
    apiPromise = new Promise((resolve, reject) => {
      const script = document.createElement('script');
      const previousCallback = window.onYouTubeIframeAPIReady;
      const timeout = setTimeout(fail, 8000);
      function fail() {
        clearTimeout(timeout);
        script.remove();
        apiPromise = undefined;
        reject(new Error('YouTube unavailable'));
      }
      window.onYouTubeIframeAPIReady = () => {
        clearTimeout(timeout);
        if (typeof previousCallback === 'function') previousCallback();
        resolve(window.YT);
      };
      script.src = 'https://www.youtube.com/iframe_api';
      script.onerror = fail;
      document.head.append(script);
    });
    return apiPromise;
  }

  function clearPlayer() {
    clearTimeout(readyTimeout);
    clearTimeout(playbackTimeout);
    if (player) {
      player.destroy();
      player = undefined;
    }
    frameHost.replaceChildren();
    frameHost.hidden = true;
  }

  function showFallback(message) {
    attempt++;
    clearPlayer();
    poster.hidden = false;
    retry.hidden = false;
    status.textContent = message;
  }

  async function startTrailer(link) {
    clearPlayer();
    const token = ++attempt;
    const video = link.dataset.trailerId;
    const title = link.dataset.trailerTitle;
    poster.hidden = false;
    retry.hidden = true;
    status.textContent = 'Indlæser den officielle trailer. Du kan også se den direkte på YouTube.';
    try {
      const yt = await loadYouTube();
      if (token !== attempt || !trailerDialog.open) return;
      const frame = document.createElement('iframe');
      frame.title = 'Officiel trailer til ' + title;
      const params = new URLSearchParams({rel:'0', enablejsapi:'1', origin:location.origin, autoplay:'1', playsinline:'1'});
      frame.src = 'https://www.youtube-nocookie.com/embed/' + video + '?' + params;
      frame.referrerPolicy = 'strict-origin-when-cross-origin';
      frame.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share';
      frame.allowFullscreen = true;
      frameHost.replaceChildren(frame);
      frameHost.hidden = false;
      // Keep the poster visible over a loading iframe until YouTube confirms readiness.
      readyTimeout = setTimeout(() => {
        if (token === attempt) showFallback('Afspilleren kunne ikke indlæses her. Brug “Se på YouTube” for at åbne traileren.');
      }, 12000);
      player = new yt.Player(frame, {events: {
        onReady: () => {
          if (token !== attempt) return;
          clearTimeout(readyTimeout);
          poster.hidden = true;
          status.textContent = 'Tryk på afspil, hvis traileren ikke starter automatisk. “Se på YouTube” er altid tilgængelig.';
          playbackTimeout = setTimeout(() => {
            if (token === attempt) showFallback('Afspilningen kunne ikke starte her. Se den officielle trailer på YouTube.');
          }, 18000);
        },
        onStateChange: event => {
          if (token !== attempt) return;
          if ([0, 1, 2].includes(event.data)) clearTimeout(playbackTimeout);
          if (event.data === 1) status.textContent = 'Den officielle trailer afspilles via YouTube.';
        },
        onAutoplayBlocked: () => {
          if (token !== attempt) return;
          clearTimeout(playbackTimeout);
          status.textContent = 'Tryk på afspil i videoen, eller vælg “Se på YouTube”.';
        },
        onError: () => {
          if (token === attempt) showFallback('YouTube kan ikke afspille traileren på denne side. Åbn den med “Se på YouTube”.');
        }
      }});
    } catch {
      if (token === attempt) showFallback('Forbindelsen til YouTube kunne ikke oprettes. Åbn traileren med “Se på YouTube”.');
    }
  }

  posterImage.addEventListener('error', () => { posterImage.hidden = true; });
  document.querySelectorAll('[data-trailer-id]').forEach(link => {
    link.addEventListener('click', event => {
      if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey || event.button !== 0) return;
      if (!/^[A-Za-z0-9_-]{11}$/.test(link.dataset.trailerId)) return;
      event.preventDefault();
      currentLink = link;
      const title = link.dataset.trailerTitle;
      document.querySelector('#trailer-dialog-title').textContent = title + ' — officiel trailer';
      document.querySelector('#trailer-poster-title').textContent = title;
      document.querySelector('#trailer-publisher').textContent = 'Udgivet af ' + link.dataset.trailerPublisher + '.';
      document.querySelector('#trailer-external').href = link.href;
      posterImage.hidden = !link.dataset.trailerThumbnail;
      if (link.dataset.trailerThumbnail) posterImage.src = link.dataset.trailerThumbnail;
      trailerDialog.showModal();
      startTrailer(link);
    });
  });
  retry.addEventListener('click', () => { if (currentLink) startTrailer(currentLink); });
  document.querySelector('#close-trailer-dialog').addEventListener('click', () => trailerDialog.close());
  trailerDialog.addEventListener('click', event => { if (event.target === trailerDialog) trailerDialog.close(); });
  trailerDialog.addEventListener('close', () => {
    attempt++;
    clearPlayer();
    currentLink?.focus();
  });
}

// Filter only the current evening; keep all source text available without JavaScript.
const programSearch = document.querySelector('#program-search');
if (programSearch) {
  const levelFilter = document.querySelector('#program-level');
  const onlyFilms = document.querySelector('#films-only');
  const resultCount = document.querySelector('#program-match-count');
  const emptyResult = document.querySelector('#program-empty');
  function applyProgramSearch() {
    const query = programSearch.value.trim().toLocaleLowerCase('da-DK');
    const level = levelFilter.value;
    let visibleCount = 0;
    document.querySelectorAll('[data-day-program]').forEach(evening => {
      evening.querySelectorAll('[data-program-entry]').forEach(entry => {
        const match = entry.textContent.toLocaleLowerCase('da-DK').includes(query)
          && (!onlyFilms.checked || entry.dataset.programKind === 'film')
          && (!level || entry.dataset.scare === level);
        entry.hidden = !match;
        if (match && !evening.hidden) visibleCount++;
      });
      evening.querySelectorAll('[data-small-hall]').forEach(hall => {
        hall.hidden = ![...hall.querySelectorAll('[data-program-entry]')].some(entry => !entry.hidden);
      });
    });
    resultCount.textContent = visibleCount === 1 ? '1 programpunkt på den valgte aften' : visibleCount + ' programpunkter på den valgte aften';
    emptyResult.hidden = visibleCount !== 0;
  }
  programSearch.addEventListener('input', applyProgramSearch);
  levelFilter.addEventListener('change', applyProgramSearch);
  onlyFilms.addEventListener('change', applyProgramSearch);
  dayButtons.forEach(button => button.addEventListener('click', applyProgramSearch));
  document.querySelector('#reset-search').addEventListener('click', () => {
    programSearch.value = '';
    levelFilter.value = '';
    onlyFilms.checked = false;
    applyProgramSearch();
    programSearch.focus();
  });
  applyProgramSearch();
}
