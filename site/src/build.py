import random, pathlib
OUT = pathlib.Path(__file__).resolve().parent.parent
css = (OUT/"src/style.css").read_text(); js = (OUT/"src/app.js").read_text()

LOGO = '<svg width="34" height="34" viewBox="0 0 34 34" aria-hidden="true"><rect width="34" height="34" rx="7" fill="#7FB24A"/><path d="M6 25 L14 9 M12 27 L20 11 M18 28 L26 12" stroke="#0B1E33" stroke-width="3" stroke-linecap="round"/><circle cx="26" cy="24" r="3.4" fill="#0B1E33"/></svg>'
CHECK = '<svg width="18" height="18" viewBox="0 0 18 18" aria-hidden="true"><circle cx="9" cy="9" r="9" fill="#7FB24A"/><path d="M5 9.4l2.6 2.5L13 6.4" stroke="#0B1E33" stroke-width="2" fill="none" stroke-linecap="round"/></svg>'

PAL = {"map":["#2C5C9A","#7FB24A","#E2B33C","#C55A3A","#5FA8C9","#8C6BB1"],
       "stubble":["#7FB24A","#4E7F25","#B9D98C","#E2B33C","#C55A3A","#7FB24A"],
       "ripener":["#E2B33C","#F0D27A","#7FB24A","#C55A3A","#E2B33C","#5FA8C9"],
       "split":["#2C5C9A","#5FA8C9","#7FB24A","#2C5C9A","#B9D98C","#5FA8C9"]}
LEG = {"map":"Variedade","stubble":"Soqueira","ripener":"Maturador","split":"Variedade"}
def screen(kind, label, seed=1):
    r = random.Random(seed)
    s = ['<svg viewBox="0 0 280 590" role="img" aria-label="%s"><rect width="280" height="590" fill="#E7EEF6"/>' % label,
         '<rect width="280" height="96" fill="#0B1E33"/><text x="20" y="74" fill="#fff" font-family="Archivo,Arial" font-weight="700" font-size="20">Fazenda exemplo</text>']
    if kind in PAL:
        s.append('<rect x="14" y="108" width="252" height="34" rx="17" fill="#fff"/><text x="30" y="130" fill="#0B1E33" font-family="Source Sans 3,Arial" font-size="14" font-weight="600">Ver por: %s ▾</text>' % LEG[kind])
        cols = PAL[kind]; y = 156
        for row in range(5):
            x = 12; h = 70 + r.randint(-8, 12)
            while x < 262:
                w = r.randint(50, 110); w = min(w, 268 - x)
                sk = r.randint(-8, 8); c = r.choice(cols)
                s.append('<polygon points="%d,%d %d,%d %d,%d %d,%d" fill="%s" stroke="#fff" stroke-width="3"/>' % (x+sk, y, x+w, y+sk//2, x+w-sk, y+h, x, y+h-sk//2, c))
                if kind == "split" and w > 80:
                    s.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#fff" stroke-width="2.5" stroke-dasharray="6 4"/>' % (x+w//2, y+4, x+w//2, y+h-4))
                x += w + 2
            y += h + 4
    else:
        y = 112
        items = ["Talhão 12 · L 01", "Talhão 14 · HoCP 96-540", "Talhão 21 · L 03-371", "Talhão 07 · Ho 12-615", "Talhão 30 · L 01-299", "Talhão 33 · HoCP 04-838"] if kind == "list" else ["Produto A · 2,0 L/ac", "Produto B · 1,5 pt/ac", "Produto C · 32 oz/ac", "Produto D · 0,5 lb/ac", "Produto E · 1,0 L/ac", "Produto F · 24 oz/ac"]
        for i, t in enumerate(items):
            s.append('<rect x="14" y="%d" width="252" height="58" rx="10" fill="#fff"/><rect x="26" y="%d" width="10" height="34" rx="3" fill="%s"/><text x="48" y="%d" fill="#0E1B2B" font-family="Source Sans 3,Arial" font-size="15" font-weight="600">%s</text>' % (y, y+12, ["#7FB24A","#2C5C9A","#E2B33C","#C55A3A","#5FA8C9","#4E7F25"][i], y+35, t))
            y += 68
    s.append('</svg>')
    return "".join(s)
def phone(kind, label, seed=1, alt=""):
    return '<div class="phone"><div class="screen">%s<p class="ph-tag">[PENDENTE: print real /app-screenshot-%s.png]</p></div></div>' % (screen(kind, alt or label, seed), kind)
def photo(cls="", note="[PENDENTE: foto real /caio.jpg]"):
    rows = "".join('<path d="M%d 600 L%d 280" stroke="#4E7F25" stroke-width="5" opacity=".55"/>' % (i*40-200, i*24+40) for i in range(16))
    return '<div class="photo %s" role="img" aria-label="Espaço para a foto de Caio Phillipi no canavial"><svg viewBox="0 0 480 600" preserveAspectRatio="none" aria-hidden="true">%s<circle cx="250" cy="250" r="44" fill="#0B1E33" opacity=".8"/><path d="M180 420 Q250 290 320 420 Z" fill="#0B1E33" opacity=".8"/></svg><p class="ph-tag">%s</p></div>' % (cls, rows, note)

SOC = {
 "Instagram":("https://www.instagram.com/yotefarmview/",'<rect x="3" y="3" width="18" height="18" rx="5" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="4" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="17.5" cy="6.5" r="1.3" fill="currentColor"/>'),
 "Facebook":("https://www.facebook.com/profile.php?id=61587002848336",'<path d="M14 8h3V4h-3c-2.8 0-4 1.8-4 4.5V11H7v4h3v6h4v-6h3l.5-4H14V9c0-.6.4-1 1-1z" fill="currentColor"/>'),
 "LinkedIn":("https://www.linkedin.com/company/yote-farmview",'<rect x="3" y="9" width="4" height="12" fill="currentColor"/><circle cx="5" cy="5" r="2.2" fill="currentColor"/><path d="M10 9h4v2c.8-1.4 2.2-2.3 4-2.3 2.6 0 3.5 1.7 3.5 4.6V21h-4v-6.6c0-1.5-.4-2.4-1.7-2.4-1.5 0-1.8 1.1-1.8 2.4V21h-4z" fill="currentColor"/>'),
 "YouTube":("https://www.youtube.com/@YoteFarmView",'<rect x="2" y="5" width="20" height="14" rx="4" fill="currentColor"/><path d="M10 9l5 3-5 3z" fill="#071525"/>'),
 "TikTok":("https://www.tiktok.com/@yotefarmview",'<path d="M14 3h3c.3 2.2 1.7 3.6 4 4v3c-1.6 0-3-.5-4-1.2V15a6 6 0 11-6-6v3.2A2.8 2.8 0 1014 15z" fill="currentColor"/>'),
}
APP = "https://apps.apple.com/us/app/yote-farmview/id6758228754"
LOGIN = "https://www.yotefarmview.app"
SITE = "https://www.yotefarmview.com"
EXT = 'target="_blank" rel="noopener"'

def header(page, home):
    h = "" if page == "home" else home
    cur = ' aria-current="page"' if page == "sobre" else ""
    return f'''<a class="pend" href="#conteudo" style="position:absolute;left:-9999px" onfocus="this.style.left='16px'" onblur="this.style.left='-9999px'">Pular para o conteúdo</a>
<header class="hdr"><div class="wrap">
<a class="logo" href="{home}" aria-label="Yote Farmview, início">{LOGO}<span>Yote Farmview<small>LOGO PROVISÓRIO</small></span></a>
<nav class="nav" id="menu" aria-label="Principal">
<a href="{h}#recursos">Recursos</a><a href="{h}#planos">Planos</a><a href="sobre.html"{cur}>Nossa história</a><a href="#contato">Contato</a>
</nav>
<div class="hdr-act"><a class="login" href="{LOGIN}" {EXT}>Entrar</a>
<a class="btn btn-primary" href="#contato" data-track="click_solicitar_demonstracao" data-where="cabecalho">Solicitar demonstração</a></div>
<button class="burger" aria-expanded="false" aria-controls="menu" aria-label="Abrir menu"><svg width="22" height="22" viewBox="0 0 22 22" aria-hidden="true"><path d="M3 6h16M3 11h16M3 16h16" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg></button>
</div></header>'''

def copyline(lbl, val, tel=False):
    href = ("tel:+12255724195" if tel else "mailto:" + val)
    return f'<div class="cline"><span class="lbl">{lbl}</span><a class="val" href="{href}">{val}</a><button type="button" class="copy" data-copy="{val}">Copiar</button></div>'

def contact(h2, txt, pid):
    return f'''<section class="band contact dark" id="contato" aria-labelledby="{pid}-t"><div class="wrap">
<div class="contact-info reveal"><p class="eyebrow">Fale com o Caio</p><h2 id="{pid}-t">{h2}</h2><p class="lead">{txt}</p>
{copyline("Telefone","(225) 572-4195",True)}{copyline("E-mail","support@yotefarmview.com")}</div>
<form class="lead-form reveal" novalidate aria-labelledby="{pid}-ft">
<h3 id="{pid}-ft">Solicitar demonstração</h3>
<div class="field"><label for="{pid}-nome">Nome</label><input id="{pid}-nome" name="nome" autocomplete="name" required aria-describedby="{pid}-nome-err"><p class="err" id="{pid}-nome-err" aria-live="polite"></p></div>
<div class="field"><label for="{pid}-tel">Telefone</label><input id="{pid}-tel" name="telefone" type="tel" inputmode="tel" autocomplete="tel" placeholder="(000) 000-0000" required aria-describedby="{pid}-tel-err"><p class="err" id="{pid}-tel-err" aria-live="polite"></p></div>
<div class="field"><label for="{pid}-email">E-mail</label><input id="{pid}-email" name="email" type="email" autocomplete="email" required aria-describedby="{pid}-email-err"><p class="err" id="{pid}-email-err" aria-live="polite"></p></div>
<div class="hp" aria-hidden="true"><label for="{pid}-hp">Site da empresa</label><input id="{pid}-hp" name="empresa_site" tabindex="-1" autocomplete="off"></div>
<button type="submit" class="btn btn-primary" data-track="click_solicitar_demonstracao" data-where="formulario">Solicitar demonstração</button>
<p class="status" role="status" tabindex="-1" hidden></p>
<p class="form-micro">Sem compromisso. O Caio responde pessoalmente.</p>
</form></div></section>'''

def footer(page, home):
    h = "" if page == "home" else home
    soc = "".join(f'<a href="{u}" {EXT} aria-label="{n}"><svg width="20" height="20" viewBox="0 0 24 24" aria-hidden="true">{p}</svg></a>' for n,(u,p) in SOC.items())
    legal = "".join(f'<a href="{SITE}/{p}" {EXT}>{t}</a>' for p,t in [("privacy-policy","Privacidade"),("terms-of-service","Termos de uso"),("cookie-policy","Cookies"),("data-privacy","Proteção de dados")])
    qr = '<svg class="qr" viewBox="0 0 21 21" role="img" aria-label="Espaço para o QR code da App Store, pendente"><rect width="21" height="21" fill="#fff"/>' + "".join(f'<rect x="{x}" y="{y}" width="1" height="1" fill="#0B1E33"/>' for x in range(21) for y in range(21) if (x*7+y*13+x*y)%5<2 and not ((x<7 and y<7) or (x>13 and y<7) or (x<7 and y>13))) + "".join(f'<rect x="{a}" y="{b}" width="7" height="7" fill="#0B1E33"/><rect x="{a+1}" y="{b+1}" width="5" height="5" fill="#fff"/><rect x="{a+2}" y="{b+2}" width="3" height="3" fill="#0B1E33"/>' for a,b in [(0,0),(14,0),(0,14)]) + '</svg>'
    return f'''<footer class="ftr"><div class="wrap">
<div class="ftr-grid">
<div><a class="logo" href="{home}">{LOGO}<span>Yote Farmview</span></a><p>Feito para a cana-de-açúcar da Louisiana, desde 2019.</p><div class="socials">{soc}</div></div>
<div><h4>Navegação</h4><a href="{h}#recursos">Recursos</a><a href="{h}#planos">Planos</a><a href="sobre.html">Nossa história</a><a href="#contato">Contato</a><a href="{LOGIN}" {EXT}>Entrar no app</a></div>
<div><h4>Contato</h4>{copyline("Telefone","(225) 572-4195",True)}{copyline("E-mail","support@yotefarmview.com")}</div>
<div><h4>Baixe o app</h4><a class="btn btn-secondary" style="color:#fff;border-color:#5C7DA6;justify-self:start" href="{APP}" {EXT} data-track="click_app_store" data-where="rodape">Baixar na App Store</a>{qr}<p class="pend" style="justify-self:start">[PENDENTE: QR real]</p></div>
</div>
<div class="ftr-bottom"><p>© 2026 Yote FarmView. Todos os direitos reservados.</p><nav aria-label="Legal">{legal}</nav>
<div class="lang" aria-label="Idioma"><a href="{SITE}/" {EXT} hreflang="en" lang="en">EN</a><span aria-current="true">PT</span><a href="{SITE}/es" {EXT} hreflang="es" lang="es">ES</a></div></div>
</div></footer>'''

def head(title, desc, extra=""):
    return f'''<title>{title}</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@75..100,600..800&family=IBM+Plex+Mono:wght@500;600&family=Source+Sans+3:wght@400;600;700&display=swap">
<style>{css}</style>
{extra}'''

def ld(obj):
    import json; return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + '</script>'
ORG = {"@context":"https://schema.org","@type":"Organization","name":"Yote Farmview","url":SITE,"email":"support@yotefarmview.com","telephone":"+1-225-572-4195","founder":{"@type":"Person","name":"Caio Phillipi"},"foundingDate":"2019","areaServed":"Louisiana, US","sameAs":[u for u,_ in SOC.values()]}
APPLD = {"@context":"https://schema.org","@type":"SoftwareApplication","name":"Yote Farmview","operatingSystem":"iOS","applicationCategory":"BusinessApplication","url":APP}

# ---------------- HOME ----------------
FAQ = [("O Yote é só para a Louisiana?","Por enquanto, atendemos produtores da Louisiana. Se você está em outro estado, fale com a gente.", True),
 ("Qual a diferença entre o Yote Base e o Precision Map?",None,False),("Posso contratar os dois?",None,False),("O que preciso levar para começar?",None,False),
 ("Quanto tempo leva o Precision Map?",None,False),("Recebo mapas impressos?",None,False),("Quantas pessoas podem usar?",None,False),
 ("Funciona sem sinal de celular?",None,False),("Com quem falo se precisar de ajuda?",None,False)]
faq_html = "".join(f'<div class="item"><h3><button aria-expanded="false" aria-controls="faq{i}" id="faqb{i}">{q}<span class="ico" aria-hidden="true">+</span></button></h3><div class="ans" id="faq{i}" role="region" aria-labelledby="faqb{i}"><div><p>{a if a else "<span class=pend>[PENDENTE: resposta do cliente]</span>"}</p></div></div></div>' for i,(q,a,_) in enumerate(FAQ))
FAQLD = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a,ok in FAQ if ok]}

def checks(items): return '<ul class="checks">' + "".join(f"<li>{CHECK}<span>{t}</span></li>" for t in items) + "</ul>"
feats = [("Mapas coloridos","Veja a fazenda inteira do jeito que precisar.","Alterne entre as visões de soqueira, variedade, colheita e maturador com um toque. Cada talhão ganha uma cor, e você sabe exatamente o que está onde, sem encostar em papel nenhum.","ripener","Mapa da fazenda colorido por maturador"),
 ("Variedades divididas","Um talhão, duas variedades. Sem problema.","Trace uma linha de divisão por número de fileiras e nomeie cada lado. O mapa de variedades continua correto mesmo quando você planta mais de uma no mesmo talhão.","split","Talhões com linha de divisão entre duas variedades"),
 ("Exportar e compartilhar","Mande um mapa limpo em segundos.","Gere um PDF profissional com a marca Yote e envie para a equipe, o proprietário da terra ou o agrônomo com um toque. Sem imprimir, sem escanear, sem explicar.","list","Lista de talhões pronta para exportar em PDF"),
 ("Registro de aplicações","Registre cada aplicação direto do campo.","Anote o produto, a dose e a unidade, sempre ligados aos talhões exatos onde foram aplicados. O histórico completo de todas as aplicações, sempre no seu bolso.","products","Lista de aplicações com produto e dose")]
feat_html = "".join(f'<article class="split reveal{" rev" if i%2 else ""}"><div class="txt"><p class="tag">{t}</p><h3>{h}</h3><p class="lead">{p}</p></div>{phone(k,a,seed=i+3)}</article>' for i,(t,h,p,k,a) in enumerate(feats))

home = f'''{head("Yote Farmview","O jeito mais simples de gerenciar seus talhões de cana. Mapas, variedades, soqueira e aplicações no celular, sem treinamento.", ld(ORG)+ld(APPLD)+ld(FAQLD))}
{header("home","./")}
<main id="conteudo">
<section class="hero" aria-labelledby="h1"><div class="rows-bg" aria-hidden="true"></div><div class="wrap">
<div class="hero-copy"><p class="eyebrow">Cana-de-açúcar · Louisiana · Desde 2019</p>
<h1 id="h1">Feito para a cana. <em>Simples de usar.</em></h1>
<p class="lead">O Yote Farmview é o jeito mais simples de gerenciar seus talhões de cana-de-açúcar. Tudo o que você precisa, no seu celular. Sem treinamento, sem manual, sem dor de cabeça.</p>
<div class="btn-row"><a class="btn btn-primary" href="#contato" data-track="click_solicitar_demonstracao" data-where="hero">Solicitar demonstração</a><a class="btn btn-secondary" href="{APP}" {EXT} data-track="click_app_store" data-where="hero">Baixar na App Store</a></div>
<p class="micro">O Caio liga para você pessoalmente. Sem call center.</p></div>
{phone("map","Mapa colorido da fazenda no app Yote",seed=1)}
</div></section>

<section class="band tight" aria-label="Números do Yote" style="padding-top:calc(var(--s5) + 40px)"><div class="wrap"><div class="stats">
<div class="stat"><b><span class="pend">[XX mil]</span>+</b><span>acres gerenciados no Yote</span></div>
<div class="stat"><b data-count="2019" data-from="2000">2019</b><span>primeiro app de mapeamento só para cana nos EUA</span></div>
<div class="stat"><b data-count="100" data-suffix="%">100%</b><span>feito para produtores, focado nos seus talhões</span></div>
<div class="stat"><b>Louisiana</b><span>nossas raízes, o próximo capítulo da sua fazenda</span></div>
</div></div></section>

<section class="band mid" aria-labelledby="prob-t"><div class="wrap split">
<div class="txt reveal"><p class="eyebrow">Por que o Yote</p><h2 id="prob-t">O produtor sempre teve a informação. Faltava um jeito simples de usá-la.</h2>
<p class="lead">Mapas de papel se perdem. Pastas se acumulam. E a maioria dos softwares agrícolas foi feita para outra cultura, não para a sua.</p>
<p class="lead" style="color:var(--ink)">O Yote foi feito para uma coisa só: cana-de-açúcar. Se você sabe usar o celular, sabe usar o Yote. Tudo no bolso, na hora em que você precisa.</p></div>
{phone("stubble","Fazenda colorida por soqueira",seed=2)}
</div></section>

<section class="band" id="recursos" aria-labelledby="rec-t"><div class="wrap">
<div class="sec-head reveal"><p class="eyebrow">Recursos</p><h2 id="rec-t">Tudo o que sua fazenda precisa. Nada que ela não precisa.</h2><p class="lead">Feito sob medida para cana-de-açúcar, sem botões extras e sem confusão.</p></div>
<div class="feat">{feat_html}</div>
<p class="center"><a class="btn btn-primary" href="#contato" data-track="click_solicitar_demonstracao" data-where="recursos">Quero ver o Yote na minha fazenda</a></p>
</div></section>

<section class="band mid" id="planos" aria-labelledby="pla-t"><div class="wrap">
<div class="sec-head reveal"><p class="eyebrow">Planos</p><h2 id="pla-t">Dois jeitos de começar.</h2><p class="lead">Nos dois, o Caio configura tudo para você. Escolha o nível de precisão.</p></div>
<div class="plans">
<article class="plan reveal"><h3>Yote Base</h3><p class="desc">Mapeamos seus talhões por imagem de satélite, ou usamos seus shapefiles, e deixamos sua conta pronta para uso.</p>
{checks(["Mapeamento por satélite ou importação dos seus shapefiles","Todos os talhões com variedade e soqueira desde o início","Acompanhe a soqueira de cada talhão a cada safra","Vários usuários com níveis de acesso diferentes","Controle da cana-semente durante a colheita","Variedades divididas dentro do talhão","Compartilhe mapas em PDF em segundos","Imprima fichas de campo para a equipe"])}
<a class="btn btn-secondary" href="#contato" data-track="click_solicitar_demonstracao" data-where="plano_base">Solicitar demonstração</a></article>
<article class="plan premium reveal"><p class="badge">Premium</p><h3>Precision Map</h3><p class="desc">Mapeamos sua fazenda a pé e de carro com receptor GPS, para a máxima precisão.</p>
<p class="note">O plano Base usa imagem de satélite para desenhar os talhões: rápido e preciso o bastante para a maioria das fazendas. O Precision Map vai além: percorremos cada talhão com um receptor GPS de alta precisão, para limites mais justos.</p>
{checks(["Cada talhão mapeado em campo com receptor GPS de alta precisão","Percorremos a fazenda inteira, sem adivinhar pelo ar","Limites mais justos do que a imagem de satélite permite","Variedades e soqueira configuradas para você no app","Cópias plastificadas do mapa, se você quiser","Entrega em poucos dias, conforme o tamanho da fazenda","Inclui acesso completo ao app por um ano"])}
<a class="btn btn-primary" href="#contato" data-track="click_solicitar_demonstracao" data-where="plano_precision">Solicitar demonstração</a></article>
</div>
<aside class="tip reveal"><b>Dica</b><p>Muitas fazendas começam pelo plano Base e acrescentam o Precision Map na cana planta nova. A cada safra, o Caio mapeia o plantio novo em campo com o receptor. Com o tempo, a fazenda inteira fica em alta precisão, sem refazer tudo de uma vez.</p></aside>
</div></section>

<section class="band dark" aria-labelledby="como-t"><div class="wrap">
<div class="sec-head reveal"><p class="eyebrow">Como funciona</p><h2 id="como-t">Começar é simples.</h2></div>
<ol class="steps">
<li class="reveal"><h3>Solicite uma demonstração</h3><p>Preencha um formulário curto com nome, telefone e e-mail. Só isso.</p></li>
<li class="reveal"><h3>Entramos em contato</h3><p>O Caio liga para você pessoalmente. Sem call center e sem e-mail automático. Uma conversa de verdade sobre a sua fazenda.</p></li>
<li class="reveal"><h3>Sua fazenda, configurada direito</h3><p>Seja pelo plano Base ou direto pelo Precision Map, deixamos tudo do jeito que você precisa.</p></li>
</ol>
<p style="margin-top:var(--s5)"><a class="btn btn-primary" href="#contato" data-track="click_solicitar_demonstracao" data-where="como_funciona">Solicitar demonstração</a></p>
</div></section>

<section class="band" data-depoimentos="3" hidden aria-labelledby="dep-t"><div class="wrap">
<div class="sec-head"><p class="eyebrow">Depoimentos</p><h2 id="dep-t">Quem planta cana e usa o Yote.</h2></div><div class="quotes"></div></div></section>

<section class="band mid" aria-labelledby="quem-t"><div class="wrap split rev">
<div class="txt reveal"><p class="eyebrow">Quem está por trás</p><h2 id="quem-t">Construído a partir do campo.</h2>
<p class="lead">Em 2019, antes de qualquer um pensar em software só para cana, Caio Phillipi já estava nos talhões, mapeando fazendas à mão.</p>
<p class="lead" style="color:var(--ink)">Quando você fala com o Yote, você fala com o Caio. E quando precisa da fazenda configurada direito, ele vai até aí.</p>
<p><a class="btn btn-secondary" href="sobre.html">Conheça nossa história</a></p></div>
{photo()}
</div></section>

<section class="band" aria-labelledby="faq-t"><div class="wrap">
<div class="sec-head reveal"><p class="eyebrow">Perguntas frequentes</p><h2 id="faq-t">Perguntas de produtores.</h2></div>
<div class="faq">{faq_html}</div></div></section>

{contact("Pronto para ter sua fazenda no bolso?","Peça uma demonstração e o Caio entra em contato pessoalmente.","h")}
</main>
{footer("home","./")}
<script>{js}</script>'''

# ---------------- SOBRE ----------------
ICONS = ['<svg width="40" height="40" viewBox="0 0 40 40" aria-hidden="true"><path d="M20 36V6M20 14c-6 0-9-4-9-8 6 0 9 3 9 8zM20 22c6 0 9-4 9-8-6 0-9 3-9 8zM20 30c-6 0-9-4-9-8 6 0 9 3 9 8z" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linejoin="round"/></svg>',
 '<svg width="40" height="40" viewBox="0 0 40 40" aria-hidden="true"><path d="M10 6h7l3 8-4 3c2 4 4 6 8 8l3-4 8 3v7c0 2-2 4-4 4C17 35 5 23 5 10c0-2 2-4 5-4z" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linejoin="round"/></svg>',
 '<svg width="40" height="40" viewBox="0 0 40 40" aria-hidden="true"><path d="M20 36s-11-11-11-20a11 11 0 0122 0c0 9-11 20-11 20z" fill="none" stroke="currentColor" stroke-width="2.4"/><circle cx="20" cy="16" r="4" fill="currentColor"/></svg>']
cards = [("Só cana","Cada botão do app existe por causa da sua cultura. Nada de recurso de outra lavoura te atrapalhando."),("Atendimento pessoal","Sem call center, sem fila de chamados, sem robô. Você fala direto com o Caio."),("Presença no campo","Quando é preciso mapear com precisão, ele vai até a sua fazenda com o receptor GPS.")]
cards_html = "".join(f'<article class="card reveal">{ICONS[i]}<h3>{t}</h3><p>{p}</p></article>' for i,(t,p) in enumerate(cards))
sobre_body = f'''{head("Sobre nós Yote Farmview","A história do Yote Farmview: o primeiro app feito só para produtores de cana dos Estados Unidos, criado por Caio Phillipi na Louisiana.", ld(ORG))}
{header("sobre","./")}
<main id="conteudo">
<section class="hero" aria-labelledby="h1"><div class="rows-bg" aria-hidden="true"></div><div class="wrap" style="padding-bottom:var(--s5)">
<div class="hero-copy"><p class="eyebrow">Nossa história</p><h1 id="h1">Construído a partir do <em>campo.</em></h1>
<p class="lead">O primeiro app feito só para quem planta cana nos Estados Unidos nasceu dentro dos canaviais, e não em um escritório.</p></div>
{photo()}
</div></section>
<section class="band" aria-label="História"><div class="wrap"><div class="story reveal">
<p>Em 2019, antes de qualquer um pensar em software feito só para cana-de-açúcar, Caio Phillipi já estava nos campos, mapeando fazendas à mão. Ele trabalhava ao lado do sogro, Bret Barrick, consultor agrícola respeitado, com décadas no setor canavieiro da Louisiana.</p>
<p>O que começou como mapas sob medida para alguns produtores virou algo maior. O Yote Farmview se tornou o primeiro app feito exclusivamente para produtores de cana dos Estados Unidos, e aqueles primeiros produtores continuam clientes até hoje.</p>
<p>O Yote não é uma empresa grande. Não tem call center, não tem fila de chamados, não tem robô de atendimento. Quando você chama, quem responde é o Caio. E quando sua fazenda precisa ser configurada direito, ele vai pessoalmente.</p>
<p><strong>Isso não é uma limitação. É justamente o ponto.</strong></p>
</div></div></section>
<section class="band mid" aria-labelledby="dif-t"><div class="wrap">
<div class="sec-head"><p class="eyebrow">O que nos diferencia</p><h2 id="dif-t">Pequeno de propósito.</h2></div>
<div class="cards3">{cards_html}</div></div></section>
<section class="band tight" aria-label="Números"><div class="wrap"><div class="stats three">
<div class="stat"><b data-count="2019" data-from="2000">2019</b><span>ano em que tudo começou</span></div>
<div class="stat"><b><span class="pend">[XX mil]</span>+</b><span>acres gerenciados</span></div>
<div class="stat"><b><span class="pend">[XX]</span></b><span>produtores atendidos, e os primeiros ainda são clientes</span></div>
</div></div></section>
<section class="band" data-depoimentos="1" hidden aria-labelledby="dep-t"><div class="wrap">
<div class="sec-head"><p class="eyebrow">Depoimento</p><h2 id="dep-t">Na palavra de quem usa.</h2></div><div class="quotes"></div></div></section>
{contact("Vamos conversar sobre a sua fazenda?","Peça uma demonstração e o Caio entra em contato pessoalmente.","s")}
</main>
{footer("sobre","./")}
<script>{js}</script>'''

(OUT/"index.html").write_text(home.replace("<main", '<main', 1).replace('<script>'+js, '<script>document.body.dataset.page="home";'+js))
sobre = ('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
         '<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style></head><body data-page="sobre">'
         + sobre_body + '</body></html>')
(OUT/"sobre.html").write_text(sobre)
print("ok", len(home), len(sobre))
