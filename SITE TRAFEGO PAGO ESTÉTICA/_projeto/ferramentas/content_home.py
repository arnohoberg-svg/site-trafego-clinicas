from lib import *

WA_HOME = MSG_GENERIC

hero_img = picture("arno-hoberg-gestor-trafego-pago", [400, 776], 776, 970,
                   "Arno Hoberg, gestor de tráfego pago para clínicas de estética, de terno azul",
                   "(min-width: 900px) 440px, 92vw", eager=True)
about_img = picture("arno-hoberg-especialista-marketing-clinicas", [480, 864], 864, 1080,
                    "Retrato de Arno Hoberg, especialista em marketing digital para clínicas estéticas",
                    "(min-width: 900px) 400px, 92vw", cls="media-rounded")

FAQ = [
    ("Quanto custa o tráfego pago para clínica de estética?",
     "<p>A gestão começa em <strong>R$ 1.200 por mês</strong>, com orçamento personalizado conforme o serviço: só Google Ads, só Meta Ads ou os dois. A verba de anúncios é separada e paga direto ao Google e à Meta; recomendamos começar com pelo menos <strong>R$ 600 por mês (R$ 20 por dia)</strong>. Veja todos os detalhes na <a href=\"@/precos/\">página de preços</a>.</p>"),
    ("Em quanto tempo aparecem os primeiros resultados?",
     "<p>Os anúncios começam a gerar visitas e contatos poucos dias depois de aprovados. As primeiras semanas servem para coletar dados e cortar desperdício; em geral, a partir do segundo ou terceiro mês a conta fica mais estável e previsível. Por isso o contrato mínimo é de 3 meses.</p>"),
    ("Qual é melhor para clínica: Google Ads ou Instagram?",
     "<p>Depende do procedimento e do momento da clínica. O <a href=\"@/google-ads-para-clinicas-esteticas/\">Google Ads</a> captura quem já está procurando (ex.: “dermatologista perto de mim”). O <a href=\"@/meta-ads-para-clinicas-esteticas/\">Meta Ads</a> gera demanda e funciona bem para procedimentos que as pessoas descobrem pelo Instagram. Com verba limitada, costumamos começar pelo canal com maior intenção e testar o segundo depois.</p>"),
    ("Vocês atendem clínicas de qualquer cidade?",
     "<p>Sim. O atendimento é 100% online, com reuniões por vídeo e comunicação pelo WhatsApp, para clínicas de todo o Brasil. As campanhas são segmentadas para a região onde estão os seus pacientes.</p>"),
    ("Vocês garantem um número de pacientes?",
     "<p>Não. Nenhum gestor sério pode garantir pacientes, porque o resultado depende também da oferta, do preço, do atendimento e da concorrência local. O que garantimos é método, transparência nos números e otimização constante. Os resultados típicos que citamos variam conforme clínica, oferta e mercado.</p>"),
    ("Os anúncios respeitam as regras do CFM e das plataformas?",
     "<p>Sim, esse é um cuidado central. Evitamos promessas de resultado, “antes e depois” fora das regras, sensacionalismo e citação de marcas de medicamentos. Explicamos os principais pontos no nosso <a href=\"@/regras-de-publicidade-para-clinicas/\">guia de regras de publicidade para clínicas</a>. A responsabilidade ética final é do profissional de saúde, por isso validamos as peças com você.</p>"),
    ("Preciso ter site para anunciar?",
     "<p>Não é obrigatório: dá para direcionar os anúncios direto para o WhatsApp. Mas uma <a href=\"@/criacao-de-sites-para-clinicas-esteticas/\">landing page bem feita</a> costuma melhorar a qualidade dos contatos, ajuda na aprovação dos anúncios de saúde e permite medir conversões com mais precisão.</p>"),
    ("Como eu acompanho os resultados?",
     "<p>Você recebe relatórios com os números que importam: investimento, cliques, custo por clique, contatos gerados e custo por contato. Também orientamos a registrar quantos contatos viraram avaliação e procedimento, que é o indicador que realmente mostra o retorno.</p>"),
]

BODY = f'''<section class="hero" aria-labelledby="titulo-principal">
<div class="container hero-grid">
<div>
<p class="eyebrow">Para clínicas de dermatologia, estética e procedimentos faciais</p>
<h1 id="titulo-principal">Tráfego pago para clínicas de estética: mais pacientes interessados, menos verba desperdiçada</h1>
<p class="lead">Campanhas enxutas no Google e no Instagram, sites que convertem e atendimento automatizado no WhatsApp, com um método feito exclusivamente para clínicas. Sem promessas mágicas, com números claros.</p>
<div class="hero-actions">{wa_btn(WA_HOME, loc="hero")}{audit_btn(loc="hero_auditoria")}</div>
<ul class="hero-points"><li>Gestão a partir de R$ 1.200/mês, com verba inicial de R$ 20/dia</li><li>Especialização exclusiva em clínicas de saúde e estética</li><li>Anúncios dentro das regras do CFM, da Anvisa, do Google e da Meta</li></ul>
</div>
<div class="hero-media">{hero_img}<p class="hero-badge"><strong>Arno Hoberg</strong>Gestor de tráfego pago para clínicas · 100% online</p></div>
</div></section>

<section class="section" aria-labelledby="problema-titulo">
<div class="container split">
<div><span class="eyebrow">O problema</span><h2 id="problema-titulo">Por que tantas clínicas investem em anúncios e não veem a agenda encher?</h2>
<p>Na maioria das contas que analisamos, o problema não é falta de verba. É verba indo para o lugar errado: cliques de curiosos, pessoas de outras cidades, termos que não têm relação com os seus procedimentos e contatos que chegam ao WhatsApp e ficam horas sem resposta.</p>
<p>Agências generalistas tratam a clínica como qualquer outro comércio. Só que publicidade em saúde tem regras próprias, o paciente pesquisa muito antes de decidir e a confiança pesa mais que o preço. Sem entender isso, a campanha até gera cliques, mas não gera avaliações marcadas.</p></div>
<div><ul class="xlist">
<li>Impulsionar posts no Instagram sem objetivo nem público definido</li>
<li>Campanhas no Google aparecendo para buscas como “curso de estética” ou “vaga de esteticista”</li>
<li>Anúncios reprovados por violar políticas de saúde e de atributos pessoais</li>
<li>Leads que não recebem resposta rápida e esfriam antes do primeiro contato</li>
<li>Relatórios cheios de métricas de vaidade e sem custo por contato</li>
<li>Site lento, confuso e sem botão claro para falar com a clínica</li>
</ul></div>
</div></section>

<section class="section section-alt" id="servicos" aria-labelledby="servicos-titulo">
<div class="container">
<div class="section-head"><span class="eyebrow">Serviços</span><h2 id="servicos-titulo">Marketing digital para clínicas estéticas, do anúncio ao WhatsApp</h2>
<p>Você pode contratar um serviço isolado ou combinar os que fazem sentido para o momento da clínica. Tudo conectado para que o interessado encontre você, entenda o seu diferencial e chame no WhatsApp.</p></div>
<div class="grid grid-3">
{service_cards()}
<article class="card card-soon"><span class="tag">Em breve</span><div class="card-icon">{ICONS["video"]}</div><h3>TikTok Ads</h3><p>Estamos preparando a operação de anúncios no TikTok para clínicas. Se tiver interesse, avise no WhatsApp.</p></article>
</div></div></section>

{how_it_works()}

{typical_results(dark=True)}

<section class="section" aria-labelledby="diferenciais-titulo">
<div class="container">
<div class="section-head"><span class="eyebrow">Diferenciais</span><h2 id="diferenciais-titulo">Por que escolher uma agência de tráfego pago só para clínicas</h2>
<p>Foco em um único nicho significa conhecer de perto as dúvidas dos pacientes, as restrições de anúncios de saúde e os procedimentos que mais trazem retorno.</p></div>
<div class="grid grid-4">
<article class="card"><h3>Método próprio</h3><p>Um processo testado em contas de clínicas: diagnóstico, estrutura enxuta, otimização semanal e escala com controle.</p></article>
<article class="card"><h3>Orçamento baixo, bem usado</h3><p>Campanhas pensadas para funcionar a partir de R$ 20 por dia, concentrando a verba onde há mais intenção de agendamento.</p></article>
<article class="card"><h3>Especialista no nicho</h3><p>Atendimento exclusivo a dermatologia, estética avançada e procedimentos faciais. Nada de copiar estratégias de outros setores.</p></article>
<article class="card"><h3>Sites feitos para vender</h3><p>Páginas rápidas e objetivas, com informações que o paciente procura e um caminho claro até o WhatsApp.</p></article>
</div></div></section>

<section class="section section-alt" aria-labelledby="captar-titulo">
<div class="container split">
<div><span class="eyebrow">Guia rápido</span><h2 id="captar-titulo">Como captar pacientes para clínica de estética com tráfego pago</h2>
<p>Captar pacientes com anúncios é um processo, não um botão de “impulsionar”. Este é o caminho que seguimos em toda conta nova:</p>
<ol>
<li><strong>Escolha os procedimentos prioritários.</strong> Comece pelos que têm boa margem, demanda na sua região e capacidade de agenda.</li>
<li><strong>Defina a região de atendimento.</strong> Segmente o raio onde estão os seus pacientes reais, não o estado inteiro.</li>
<li><strong>Combine intenção e descoberta.</strong> Use o Google para quem já procura e o Instagram para apresentar a clínica a quem ainda não conhece.</li>
<li><strong>Envie o clique para um destino preparado.</strong> Uma landing page clara ou o WhatsApp com mensagem pronta e resposta rápida.</li>
<li><strong>Meça o que importa.</strong> Custo por contato e quantos contatos viraram avaliação, não apenas curtidas e cliques.</li>
<li><strong>Otimize toda semana.</strong> Corte termos e públicos que não convertem e reinvista nos que trazem pacientes.</li>
</ol></div>
<div><h3>Tráfego pago para dermatologistas e clínicas de harmonização</h3>
<p>Dermatologistas costumam ter boa demanda de busca para consultas e tratamentos de pele, o que favorece campanhas de pesquisa no Google. Já procedimentos faciais e de harmonização dependem mais de confiança e de conteúdo educativo, o que favorece o Instagram — sempre sem prometer resultados e sem imagens que contrariem as regras do conselho.</p>
<p>Em ambos os casos, o atendimento faz diferença: responder em minutos, e não em horas, costuma ser o que separa um contato de uma avaliação marcada. É aí que entra a <a href="@/automacao-whatsapp-para-clinicas/">automação de WhatsApp para clínicas</a>.</p>
<p>Quer saber onde a sua conta está perdendo dinheiro hoje? Peça uma <a href="@/auditoria-gratuita-de-anuncios/">auditoria gratuita de anúncios</a>.</p></div>
</div></section>

<section class="section" id="precos" aria-labelledby="precos-titulo">
<div class="container split">
<div><span class="eyebrow">Investimento</span><h2 id="precos-titulo">Quanto investir em tráfego pago para clínica?</h2>
<p><strong>Resposta curta:</strong> a gestão começa em R$ 1.200 por mês e a verba de anúncios recomendada é de no mínimo R$ 600 por mês (R$ 20 por dia), paga direto às plataformas. O contrato mínimo é de 3 meses.</p>
<div class="table-wrap"><table class="price-table"><caption class="visually-hidden">Resumo de investimento</caption>
<thead><tr><th scope="col">Item</th><th scope="col">Valor</th></tr></thead><tbody>
<tr><td>Gestão de tráfego (Google Ads, Meta Ads ou ambos)</td><td>A partir de R$ 1.200/mês</td></tr>
<tr><td>Verba de anúncios (paga ao Google/Meta)</td><td>Mínimo recomendado R$ 600/mês</td></tr>
<tr><td>Site ou landing page</td><td>Sob orçamento</td></tr>
<tr><td>Automação de WhatsApp</td><td>Sob orçamento</td></tr>
<tr><td>Contrato mínimo</td><td>3 meses</td></tr>
</tbody></table></div>
<p>O valor final depende dos canais e do número de procedimentos trabalhados. Veja a explicação completa em <a href="@/precos/">preços de tráfego pago para clínicas</a>.</p></div>
<div class="form-card"><h3 id="orcamento-titulo">Monte seu orçamento em 30 segundos</h3><p class="note">Marque o que você precisa e receba a mensagem pronta no WhatsApp.</p>{quote_form("orcamento-home")}</div>
</div></section>

<section class="section section-alt" aria-labelledby="sobre-titulo">
<div class="container split split-media">
<div>{about_img}</div>
<div><span class="eyebrow">Quem está por trás</span><h2 id="sobre-titulo">Prazer, Arno Hoberg</h2>
<p>Sou gestor de tráfego pago e decidi atender um único tipo de negócio: clínicas de dermatologia, estética avançada e procedimentos faciais. Essa escolha me permite conhecer a fundo o comportamento do paciente, os procedimentos que mais geram retorno e as regras que limitam a publicidade em saúde.</p>
<!-- CONFIRMAR: dado "60 clientes" — é média de contatos no primeiro mês ou total de clientes atendidos? Não publicar até validar. -->
<p>Trabalho com campanhas enxutas, comunicação direta e relatórios que qualquer dono de clínica entende. Você fala comigo, e não com um atendente que repassa recados.</p>
<p><a href="@/sobre/">Conheça minha forma de trabalhar</a></p></div>
</div></section>

<section class="section" aria-labelledby="regras-titulo">
<div class="container split">
<div><span class="eyebrow">Conformidade</span><h2 id="regras-titulo">Anúncios dentro das regras do CFM, da Anvisa e das plataformas</h2>
<p>Publicidade em saúde exige cuidado redobrado. Conselhos profissionais limitam promessas e certas imagens, a Anvisa restringe a divulgação de medicamentos como a toxina botulínica, e Google e Meta têm políticas específicas para serviços de saúde e estética.</p></div>
<div><p>Por isso, cada campanha é criada para informar sem prometer, com linguagem ética e sem expor pacientes. Reunimos os pontos principais em um guia gratuito: <a href="@/regras-de-publicidade-para-clinicas/">regras de publicidade para clínicas de estética</a>.</p>
<p class="note">O guia é informativo e não substitui orientação jurídica nem as normas oficiais do seu conselho.</p></div>
</div></section>

{testimonials_placeholder()}

[[FAQ]]

{cta_band("Vamos ver o que dá para melhorar na sua clínica?", "Conte rapidamente sobre a sua clínica e receba uma orientação inicial sem compromisso.", WA_HOME, "cta_final", ("auditoria-gratuita-de-anuncios/", "Pedir auditoria gratuita"))}
'''

PAGES = [{
    "path": "",
    "title": "Tráfego Pago para Clínicas de Estética | Arno Hoberg",
    "desc": "Tráfego pago para clínicas de estética e dermatologia: Google Ads, Meta Ads, sites e automação de WhatsApp. Peça sua auditoria gratuita pelo WhatsApp.",
    "body": BODY,
    "faq": FAQ,
    "wa_msg": WA_HOME,
    "schema": [professional_service_schema(), person_schema()],
    "preload": ('<link rel="preload" as="image" type="image/avif" fetchpriority="high" '
                'imagesrcset="@/assets/img/arno-hoberg-gestor-trafego-pago-400.avif 400w, @/assets/img/arno-hoberg-gestor-trafego-pago-776.avif 776w" '
                'imagesizes="(min-width: 900px) 440px, 92vw">\n'),
}]
