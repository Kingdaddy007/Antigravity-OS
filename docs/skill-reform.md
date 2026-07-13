# Skill Reform Notes

The reform changed the skills themselves; it was not only a folder rearrangement.

- Skill folders and frontmatter use portable hyphen-case names.
- Activation rules and exclusions were made explicit so a skill is not loaded for unrelated work.
- Host-specific UI metadata moved into `agents/openai.yaml`.
- Detailed recipes, dated research, examples, and large taxonomies moved into conditional `references/` files.
- Broken absolute paths, dead sibling routes, unsupported tool names, and unresolved tokens were repaired.
- General engineering is the default profile; spatial-only guidance is selected only when the request qualifies.
- Volatile claims are marked with a source and verification date or treated as unverified.

To inspect the actual skill-level edits, run:

```bash
git diff --stat -- global/skills
git diff -- global/skills
python global/scripts/os.py validate
```

The new [video-generation skill](../global/skills/video-generation/SKILL.md) demonstrates the target format: activation, boundaries, provider-neutral routing, conditional references, output shape, and verification gates.
