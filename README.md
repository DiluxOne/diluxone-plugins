# DiluxOne Plugins AI

The DiluxOne catalog of plugins for coding agents. Add it once and install any of its plugins. Each plugin installs from its own repository.

## Claude Code

```
/plugin marketplace add DiluxOne/diluxone-plugins-ai
```

Then install the plugins you want:

```
/plugin install daw@diluxone-plugins-ai
/plugin install diluxone-mermaid@diluxone-plugins-ai
```

New plugins added to this catalog show up for everyone who already added it. To update: `/plugin marketplace update diluxone-plugins-ai`.

## GitHub Copilot CLI

Copilot CLI reads the same catalog as Claude Code:

```
copilot plugin marketplace add DiluxOne/diluxone-plugins-ai
copilot plugin install daw@diluxone-plugins-ai
copilot plugin install diluxone-mermaid@diluxone-plugins-ai
```

## Codex

```
codex plugin marketplace add DiluxOne/diluxone-plugins-ai
```

Then install `daw` or `diluxone-mermaid` from the `diluxone-plugins-ai` marketplace in Codex's plugins directory. To update: `codex plugin marketplace upgrade diluxone-plugins-ai`.

## Cursor, Gemini CLI and OpenCode

These tools install a plugin from its own repository, not from a catalog. Each plugin's README has the steps:

- Cursor: clone the plugin's repository into `~/.cursor/plugins/local/<plugin>`, then restart Cursor.
- Gemini CLI: `gemini extensions install https://github.com/DiluxOne/<repository>`.
- OpenCode: the plugin's README, OpenCode section.

## Moving from the old catalog

This catalog used to be `diluxone/diluxone-plugins`, whose marketplace is named `diluxone`, and DAW had a marketplace of its own, `dilux` (plugin `ddw`). Neither is kept. If you added either, remove it and add this one again:

```
/plugin marketplace remove diluxone
/plugin marketplace remove dilux
/plugin marketplace add DiluxOne/diluxone-plugins-ai
```

Then install the plugins again from `diluxone-plugins-ai`, as above (`ddw@dilux` is now `daw@diluxone-plugins-ai`).

## Plugins

| Plugin | What it does | Tools | Repo |
| --- | --- | --- | --- |
| `daw` | An agent-driven development pipeline: phases in order, gates enforced by hooks outside the model, auditors that did not write the code they review, and state that survives closing the session. | Claude Code, Copilot CLI, Codex (catalog); Cursor, Gemini CLI, OpenCode (its README) | [DiluxOne/dilux-agentic-workflow](https://github.com/DiluxOne/dilux-agentic-workflow) |
| `diluxone-mermaid` | Create, edit and validate mermaid diagrams that never break: lint, the real mermaid 10, 11 and 12 parser, render geometry and visual review. | Claude Code, Copilot CLI, Codex (catalog); Cursor, Gemini CLI, OpenCode (its README) | [DiluxOne/diluxone-mermaid](https://github.com/DiluxOne/diluxone-mermaid) |

## License

[MIT](LICENSE)
