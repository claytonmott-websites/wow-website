/* WOW — Wealth on Wheels · site behaviour (no dependencies) */
(function () {
  const header = document.querySelector('.site-header');

  /* Header border once the page scrolls */
  const onScroll = () => header && header.classList.toggle('scrolled', window.scrollY > 8);
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  /* Platform mega menu */
  const megaBtn = document.querySelector('[data-mega]');
  const mega = document.getElementById('mega');
  function setMega(open) {
    if (!megaBtn || !mega) return;
    megaBtn.setAttribute('aria-expanded', String(open));
    mega.hidden = !open;
  }
  if (megaBtn && mega) {
    megaBtn.addEventListener('click', () => setMega(mega.hidden));
    document.addEventListener('click', ev => {
      if (!mega.hidden && !ev.target.closest('.has-mega')) setMega(false);
    });
    mega.parentElement.addEventListener('focusout', ev => {
      if (!mega.parentElement.contains(ev.relatedTarget)) setMega(false);
    });
  }

  /* Mobile drawer */
  const menuBtn = document.querySelector('.menu-btn');
  const drawer = document.getElementById('drawer');
  function setDrawer(open) {
    if (!menuBtn || !drawer) return;
    drawer.hidden = !open;
    menuBtn.setAttribute('aria-expanded', String(open));
    menuBtn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    menuBtn.innerHTML = open
      ? '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>'
      : '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>';
    document.body.classList.toggle('menu-open', open);
    if (open) { const first = drawer.querySelector('a,summary'); if (first) first.focus(); }
  }
  if (menuBtn && drawer) {
    menuBtn.addEventListener('click', () => setDrawer(drawer.hidden));
    drawer.addEventListener('click', ev => { if (ev.target.closest('a')) setDrawer(false); });
    window.addEventListener('resize', () => { if (window.innerWidth > 1080 && !drawer.hidden) setDrawer(false); });
  }

  document.addEventListener('keydown', ev => {
    if (ev.key !== 'Escape') return;
    if (mega && !mega.hidden) { setMega(false); megaBtn.focus(); }
    if (drawer && !drawer.hidden) { setDrawer(false); menuBtn.focus(); }
  });

  /* Forms: client-side validation. Connect data-endpoint to a real handler before launch. */
  document.querySelectorAll('form[data-form]').forEach(form => {
    form.setAttribute('novalidate', '');
    form.addEventListener('submit', async ev => {
      ev.preventDefault();
      let firstBad = null;
      form.querySelectorAll('.field').forEach(field => {
        const input = field.querySelector('input,select,textarea');
        if (!input) return;
        const bad = !input.checkValidity();
        field.classList.toggle('invalid', bad);
        input.setAttribute('aria-invalid', String(bad));
        if (bad && !firstBad) firstBad = input;
      });
      if (firstBad) { firstBad.focus(); return; }

      const endpoint = form.dataset.endpoint;
      const submit = form.querySelector('[type="submit"]');
      if (submit) { submit.disabled = true; submit.textContent = 'Sending…'; }
      try {
        if (endpoint) {
          const res = await fetch(endpoint, { method: 'POST', body: new FormData(form), headers: { Accept: 'application/json' } });
          if (!res.ok) throw new Error('Request failed');
        }
        const done = document.querySelector(form.dataset.done);
        form.hidden = true;
        if (done) { done.hidden = false; done.focus(); }
      } catch (err) {
        if (submit) { submit.disabled = false; submit.textContent = 'Try again'; }
        const msg = form.querySelector('[data-form-error]');
        if (msg) msg.hidden = false;
      }
    });
    form.querySelectorAll('input,select,textarea').forEach(input =>
      input.addEventListener('input', () => {
        const field = input.closest('.field');
        if (field && field.classList.contains('invalid') && input.checkValidity()) {
          field.classList.remove('invalid');
          input.setAttribute('aria-invalid', 'false');
        }
      }));
  });

  /* Preselect the role on the contact form from ?role= links */
  const role = new URLSearchParams(location.search).get('role');
  const roleSelect = document.getElementById('role');
  if (role && roleSelect) {
    const opt = [...roleSelect.options].find(o => o.value === role);
    if (opt) roleSelect.value = role;
  }

  document.querySelectorAll('[data-year]').forEach(el => { el.textContent = new Date().getFullYear(); });
})();
