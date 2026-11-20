/* f1-portao-1.js — inicialização do deck e "retomar de onde parou".
   O professor para onde quiser e continua na aula seguinte; o deck guarda a tela. */

(function () {
  var CHAVE = 'f1-portao-1:posicao';
  var botao = document.querySelector('.retomar');

  Reveal.initialize({
    hash: true,
    history: true,
    transition: 'fade',
    transitionSpeed: 'fast',
    controls: true,
    controlsLayout: 'bottom-right',
    progress: true,
    slideNumber: false,
    width: 1280,
    height: 720,
    margin: 0.07,
    math: {
      mathjax: 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js',
      config: 'tex-chtml'
    }
  });

  function telas() {
    return Reveal.getSlides().map(function (el, i) {
      return {
        indice: i,
        tela: el.getAttribute('data-tela'),
        bloco: el.getAttribute('data-bloco'),
        h: parseInt(el.getAttribute('data-h'), 10),
        v: parseInt(el.getAttribute('data-v'), 10)
      };
    });
  }

  function salvar() {
    var indice = Reveal.getIndices();
    try {
      localStorage.setItem(CHAVE, JSON.stringify({ h: indice.h, v: indice.v }));
    } catch (e) { /* modo privado: seguir sem retomar */ }
  }

  function oferecerRetomar() {
    if (!botao) { return; }
    var bruto = null;
    try { bruto = localStorage.getItem(CHAVE); } catch (e) { return; }
    if (!bruto) { return; }
    var pos;
    try { pos = JSON.parse(bruto); } catch (e) { return; }
    if (!pos || (pos.h === 0 && pos.v === 0)) { return; }

    var alvo = null;
    telas().forEach(function (t) {
      if (t.h === pos.h && t.v === (pos.v || 0)) { alvo = t; }
    });
    if (!alvo) { return; }

    botao.textContent = 'retomar · tela ' + alvo.tela + ' · ' + alvo.bloco;
    botao.classList.add('visivel');
    botao.addEventListener('click', function () {
      Reveal.slide(pos.h, pos.v || 0);
      botao.classList.remove('visivel');
    });
  }

  Reveal.on('ready', function () {
    oferecerRetomar();
    salvar();
  });
  Reveal.on('slidechanged', salvar);
})();
