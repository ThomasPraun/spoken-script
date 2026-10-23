# Skill de guiones humanos para video

Oct 22, 2026 · @Thomas Praun

## Propósito

Queremos un skill propio que escriba guiones de video que suenen dichos por una persona real, con mi voz, y que enganchen de principio a fin. No alcanza con que el texto "no suene a IA": tiene que funcionar hablado frente a cámara.

El skill debe lograr cuatro cosas:

1. **Enganchar:** un gancho fuerte en los primeros segundos y una estructura que sostenga la atención hasta el cierre.
2. **Sonar humano:** sin muletillas de IA (frases infladas, listas de tres, conclusiones genéricas, vocabulario de folleto).
3. **Sonar a mí:** mi ritmo, mis palabras y mi registro, en español rioplatense.
4. **Funcionar en voz alta:** frases cortas, fáciles de pronunciar, con pausas y énfasis marcados para grabar.

## El problema

Los guiones que genera un modelo suelen fallar en tres frentes, y ningún skill existente cubre los tres a la vez.

- **Suenan a IA:** tienden a la frase más probable, con adjetivos grandilocuentes, transiciones de manual y cierres tipo "el futuro es prometedor".
- **Suenan genéricos:** sin voz propia, cualquier creador podría decirlo igual.
- **Están escritos para leer, no para decir:** oraciones largas, subordinadas, palabras difíciles de pronunciar y nada de ritmo oral.

Los humanizadores atacan el primer punto, los escritores de guion atacan la estructura, y casi ninguno atiende la oralidad ni el español rioplatense.

## Humanizadores

Sacan los patrones de escritura de IA. La referencia es blader/humanizer; casi todo lo demás es un fork o una adaptación.

| Skill | Idioma | Qué aporta | Instalación |
| --- | --- | --- | --- |
| [blader/humanizer](https://github.com/blader/humanizer) | Inglés | 29 patrones de IA basados en la guía "Signs of AI writing" de Wikipedia; calibración de voz con muestras propias; auditoría final y segunda pasada | `npx skills add blader/humanizer --skill humanizer` |
| [jooray/humanizer](https://github.com/jooray/humanizer) | Inglés | Fork del anterior con modo detección: señala frases sospechosas sin reescribir | `npx skills add jooray/humanizer --global` |
| [Hainrixz/humanizalo](https://github.com/Hainrixz/humanizalo) | Español | Puntaje de humanización antes y después; adapta a tu voz; comando `/humanizalo` | `git clone https://github.com/Hainrixz/humanizalo.git ~/.claude/skills/humanizalo` |
| [humaniza](https://claudskills.com/skills/humaniza/) | Español (México) | Editor de estilo que quita tics de IA sin cambiar el contenido | Copiar el SKILL.md a `~/.claude/skills/humaniza/` |
| [lukeslp/skill-humanize](https://github.com/lukeslp/skill-humanize) | Inglés | 15 categorías con puntaje de confianza: corrige lo seguro, sugiere lo dudoso | `claude plugin add lukeslp/skill-humanize` |
| [humanize (pproenca)](https://www.skills.sh/aaaaqwq/claude-code-skills/humanize) | Inglés | Versión corta basada en la misma guía de Wikipedia | Desde skills.sh |

Limitación común: todos están pensados para texto escrito (blogs, emails, documentación), no para guion hablado.

## Escritores de guion

Arman la estructura: gancho, desarrollo, retención y cierre. Ninguno está en español ni pone el foco en la voz propia.

### Video largo (YouTube)

| Skill | Qué aporta |
| --- | --- |
| [youtube-script-writer (raroque/boop-agent)](https://skillselion.com/skills/raroque/boop-agent/youtube-script-writer) | Convierte tema, esquema o investigación en guion de 5 a 8 min; busca datos antes de escribir y no inventa cifras ni citas |
| [script-writer (eddiebe147/claude-settings)](https://skills.sh/eddiebe147/claude-settings/script-writer) | Guiones pensados para sonar bien leídos en voz alta; YouTube, podcast y presentaciones |
| [video-script (sugarforever/01coder-agent-skills)](https://claudemarketplaces.com/skills/sugarforever/01coder-agent-skills/video-script) | Paquete de publicación: guion hablado, post de blog y descripciones con tags por plataforma |
| [youtube-script-writer (mohitagw15856)](https://claudskills.com/skills/youtube-script-writer/) | Guiones de alta retención con indicaciones de imagen y audio |
| [script-writer (modelscope.cn)](https://www.skills.sh/site/modelscope.cn/script-writer) | Aprende tu estilo y lo mantiene entre guiones |
| [scriptwriting (smithery.ai)](https://skills.sh/site/smithery.ai/scriptwriting) | Explicadores, testimonios, liderazgo de opinión y videos de producto |
| [Text-to-Video (Pictory)](https://docs.pictory.ai/claude-skills/overview) | Escribe el guion, arma escenas y renderiza el video vía la API de Pictory (requiere cuenta) |

### Video corto (Reels, TikTok, Shorts)

| Skill | Qué aporta |
| --- | --- |
| [viral-short-form (vyralcontent)](https://skillselion.com/skills/vyralcontent/content-skills/viral-short-form) | El más instalado (más de 132.000); estructura gancho, escalada, payoff y CTA; plantillas de guion |
| [viral-hooks (vyralcontent)](https://vibeindex.ai/skills/vyralcontent/content-skills/viral-hooks) | Solo los primeros 1 a 3 segundos: gancho visual, verbal y texto en pantalla |
| [short-form-script (mohitagw15856)](https://claudeskills.info/skills/mohitagw15856/pm-claude-skills/short-form-script/) | Guion de 15 a 60 s armado para tiempo de visualización y re-vistas |
| [reel-script-writer (jmsktm)](https://skillselion.com/skills/jmsktm/claude-settings/reel-script-writer) | Reels de 15 a 90 s con apertura, beats de escena y CTA |
| [short-form-video (cdeistopened)](https://skills.sh/cdeistopened/content-os/short-form-video) | Flujo completo de concepto a publicación, con prototipado rápido |
| [video-marketing (kostja94)](https://skills.cat/skills/kostja94/marketing-skills/video-marketing) | Estrategia y guion para corto y largo según objetivo y plataforma |
| [04-script-video-global (minhnv0807)](https://www.skills.sh/minhnv0807/fullstack-mkt-skills/04-script-video-global) | Dos variantes A/B de guion, guía de rodaje, captions y puntaje viral |
| [visual-hook (postplusai)](https://www.skills.sh/postplusai/hook-skills/visual-hook) | Refuerza la apertura visual de videos y carruseles |

El repositorio completo de vyralcontent está en [github.com/vyralcontent/content-skills](https://github.com/vyralcontent/content-skills) (incluye skills por plataforma, ideas y captions).

## Qué tomar y qué falta

Nuestro skill toma lo mejor de tres fuentes y agrega lo que ninguna trae.

| Fuente | Qué tomar |
| --- | --- |
| blader/humanizer | El catálogo de patrones de IA, la calibración de voz con muestras propias y la auditoría final con segunda pasada |
| jooray/humanizer | El modo detección para revisar un guion sin reescribirlo |
| Hainrixz/humanizalo y humaniza | Los patrones de IA propios del español (no son iguales a los del inglés) |
| viral-short-form y viral-hooks | Estructura gancho → escalada → payoff → CTA y el gancho en tres capas |
| youtube-script-writer (raroque) | Investigar antes de escribir y no inventar datos |
| script-writer (eddiebe147) | El criterio de escribir para ser dicho, no leído |

**Lo que falta en todos:**

- Reglas de oralidad: frases cortas, una idea por oración, palabras fáciles de pronunciar.
- Marcas de interpretación: pausas, énfasis, cambios de ritmo, indicaciones de imagen.
- Español rioplatense: voseo, giros locales, muletillas naturales en su justa medida.
- Una prueba de lectura en voz alta antes de dar el guion por terminado.

## Diseño propuesto

Un solo skill que escribe, humaniza y prepara el guion para grabar, en cinco pasos.

1. **Brief:** pide tema, formato (corto o largo), duración, plataforma, público y objetivo. Si el tema necesita datos, los busca y no inventa.
2. **Ganchos:** propone 3 a 5 aperturas distintas y elegimos una.
3. **Borrador:** escribe con la estructura del formato (gancho → escalada → payoff → CTA en corto; actos con reenganches en largo).
4. **Humanizar y dar voz:** pasa el borrador por los patrones anti-IA en español y lo ajusta a mis muestras de voz.
5. **Pasada oral:** acorta frases, marca pausas y énfasis, agrega indicaciones de imagen y revisa que se pueda decir de corrido.

Estructura de carpetas sugerida:

```
guion-humano/
├── SKILL.md              # propósito, cuándo usarlo y los 5 pasos
├── references/
│   ├── mi-voz.md         # transcripciones y rasgos de cómo hablo
│   ├── patrones-ia-es.md # tics de IA en español a evitar
│   ├── estructuras.md    # esqueletos para corto y largo
│   └── oralidad.md       # reglas para escribir para ser dicho
└── assets/
    └── plantilla-guion.md
```

### Próximos pasos

- [ ] Juntar 3 o 4 transcripciones de videos míos (o de creadores cuyo estilo quiero)
- [ ] Leer los SKILL.md de blader/humanizer, viral-short-form y script-writer (eddiebe147) y extraer reglas
- [ ] Escribir patrones-ia-es.md con los tics de IA propios del español
- [ ] Redactar el SKILL.md con skill-creator
- [ ] Probarlo con 3 guiones reales y ajustar

Antes de instalar o copiar cualquier skill de la comunidad, conviene leer su SKILL.md: la calidad y la seguridad varían mucho entre forks.
