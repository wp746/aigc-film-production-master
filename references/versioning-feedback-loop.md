# Versioning And Feedback Loop

Use this whenever the user reviews a module, changes direction, rejects an output, asks to revise part of the system, or wants a new version.

## Rule

Do not let revisions destroy approved work. Version modules and regenerate only affected downstream artifacts when possible.

## Version Units

| Unit | Example |
|---|---|
| Creative module | `CREATIVE_v002` |
| Script | `SCRIPT_v003` |
| AIGC director module | `DIRECTOR_v002` |
| Handoff | `HANDOFF_v002` |
| Asset prompt | `A01_v003` |
| Storyboard prompt | `S03_v002` |
| Seedance prompt | `SEG03_v004` |
| Post plan | `POST_v002` |

## Change Impact Map

| User Change | Usually Affects |
|---|---|
| premise/theme | creative, script, director, all prompts |
| character identity | character assets, storyboards containing character, Seedance refs |
| wardrobe/state | character state, affected segments only |
| scene geography | scene board, storyboards in that scene, Seedance prompts |
| prop design | prop board, hand-use shots, continuity |
| style/look | global look lock, all visual prompts |
| segment action | affected storyboard and Seedance prompt |
| dialogue | script lock, Seedance audio timing, subtitles/post |
| exact text/UI | text plate, post overlay, clean-frame constraints |

## Revision Response

When updating:

```markdown
## Revision Applied
- Changed module:
- New version:
- Affected prompts:
- Preserved modules:
- Regenerated files:
```

Keep this summary short for the user. The version table can remain backstage unless requested.
