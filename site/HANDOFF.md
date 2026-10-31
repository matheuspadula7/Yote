# Handoff: site PT do Yote Farmview

## Onde está tudo
- Branch: `ccr-28baf659-fzxdt9` (repo `matheuspadula7/yote`), pasta `site/`.
- Artefato publicado (privado): https://claude.ai/artifact/YbHKU4Kr4VZiARhHDcu3Dk
  Para atualizar, publique `site/index.html` com `url` desse artefato e `files: {"sobre.html": "site/sobre.html"}`. Leia o artefato antes (`action: read`).
- Prompt original (doc): https://claude.ai/artifact/4Jb4jjy2r18brwzqi8d8PD. É a especificação completa e deve ser seguida.

## Como o código está organizado
- `site/src/style.css`: tokens (`:root`) e todo o CSS. Identidade PROVISÓRIA em azul-marinho (`--navy-*`), verde-cana nos botões (`--cane`), fontes Archivo / Source Sans 3 / IBM Plex Mono.
- `site/src/app.js`: menu, FAQ, botões de copiar, contador, eventos (`dataLayer`), formulário. Constantes `LEAD_ENDPOINT` e `DEPOIMENTOS` no topo.
- `site/src/build.py`: gera `site/index.html` e `site/sobre.html` com CSS e JS inline. Todo o conteúdo (textos, FAQ, planos, placeholders) está aqui. **Edite os arquivos em src/ e rode `python3 site/src/build.py`.** Não edite os HTML gerados à mão.

## Estado
- Feito: Home (10 seções + cabeçalho e rodapé) e Sobre nós (6 seções), responsivas e testadas em 1280 e 375 px.
- Formulário em modo demonstração (sem capacidade `db`, porque as regras do banco expõem os leads a quem pode gravar).
- A sessão na nuvem não conseguiu acessar www.yotefarmview.com (bloqueio de rede). Por isso nada foi extraído do site real.

## Próximos passos
1. Baixar o HTML e o CSS de https://www.yotefarmview.com (`/_next/static/css/`) e extrair as cores, as fontes, o raio de borda e o espaçamento. Atualizar os tokens em `style.css`. A marca é em tons de azul escuro.
2. Baixar `/logo.png`, `/app-screenshot-{map,stubble,ripener,split,list,products}.png`, `/caio.jpg`, `/app-store-qr.png` e `/og-image.png`. Converter para WebP (largura máxima de 1600 px, até 400 KB cada), salvar em `site/img/` e publicar como `files` do artefato.
3. Em `build.py`, trocar `phone()`, `photo()`, o QR SVG e o `LOGO` pelas imagens reais (`<img>` com width/height e `loading="lazy"`, exceto no hero).
4. Buscar as respostas do FAQ no site atual e traduzir para pt-BR. Atualizar `FAQ` em `build.py`, marcando `True` nas respostas confirmadas, para que entrem no JSON-LD.
5. Fotos de banco (Unsplash/Pexels, só canavial) são opcionais. Listar os créditos.
6. Rodar o build, conferir em 375 e 1280 px e republicar no mesmo artefato.

## Pendências do cliente
Número de acres `[XX mil]`, número de produtores `[XX]`, depoimentos reais e respostas do FAQ que não estiverem no site.

## Para o site no ar
`sitemap.xml`, `robots.txt`, canonical, `hreflang` EN/ES, banner de cookies com o botão de recusar igual ao de aceitar, GA4/Meta Pixel por variável de ambiente e `LEAD_ENDPOINT` apontando para o serviço de e-mail.
