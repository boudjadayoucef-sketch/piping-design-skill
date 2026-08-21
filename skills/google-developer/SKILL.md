---
name: google-developer
description: Write, review, and improve developer documentation using the current Google Developer Documentation Style Guide principles. Use for technical documentation, API docs, tutorials, how-to guides, reference pages, READMEs, and documentation edits.
---

# Google Developer Documentation Style

Use this skill to produce clear, consistent, accessible developer documentation inspired by the official Google Developer Documentation Style Guide.

## Core behavior

1. Follow project-specific documentation rules first.
2. Then apply this skill.
3. Prefer clarity and consistency over rigid rule-following.
4. Write for developers and other technical practitioners.
5. When the project has a defined terminology or style sheet, preserve it consistently.

## Voice and tone

- Be conversational, friendly, respectful, and professional.
- Address the reader as **you** and **your** when appropriate.
- Prefer active voice.
- Use direct, actionable instructions.
- Keep sentences concise and easy to scan.
- Write for a global audience.
- Avoid slang, clichés, buzzwords, unnecessary jargon, figurative language, and culturally specific references.
- Avoid filler such as “please note,” “at this time,” “it’s easy,” and “simply.”
- Avoid unnecessary exclamation marks.
- Do not pre-announce what the documentation is about; start with useful information.

## Organization

- Put the most useful information first.
- Use descriptive, sentence-case headings.
- Use one clear H1 title, followed by H2/H3 sections.
- Use numbered lists for sequences and procedures.
- Use bulleted lists for unordered information.
- Break long procedures into explicit steps.
- Put conditions before instructions when a condition changes what the reader should do.
- Prefer short paragraphs and scannable structure.

## Language

- Use standard American English unless the project specifies another variant.
- Use precise technical terminology.
- Define unfamiliar terms when necessary.
- Prefer concrete verbs over nominalizations.
- Avoid unnecessary repetition.
- Use consistent terminology for the same concept.
- Use serial commas.
- Use “and” instead of “&”, except when reproducing an actual UI label or proper name.
- Use unambiguous dates.

## Formatting

- Use `code font` for code, filenames, commands, methods, classes, variables, HTTP status codes, placeholders, and literal values when appropriate.
- Use **bold** for UI elements when the documentation convention calls for it.
- Use sentence case for titles and headings.
- Do not manually override fonts, sizes, or colors.
- Use descriptive link text rather than “click here.”
- Provide useful alt text for meaningful images.

## Code samples

- Introduce code samples with a sentence or short paragraph explaining what the reader will see.
- Keep examples focused on the task.
- Follow the relevant programming-language style guide.
- Prefer readable formatting and consistent indentation.
- Keep long lines manageable; Google’s guidance commonly recommends wrapping code samples at 80 characters.
- Explain non-obvious code rather than narrating every line.
- Use realistic names and values.
- Make placeholders unmistakable, for example `PROJECT_ID` or `YOUR_API_KEY`.

## Procedures

For a task that has an ordered sequence:

1. State any prerequisite or condition first.
2. Give one action per step when possible.
3. Start steps with clear imperative verbs.
4. Show commands and expected values in code formatting.
5. Explain the result when it helps the reader verify success.
6. Put troubleshooting after the main successful path.

## Accessibility and inclusivity

- Use plain, direct language.
- Avoid ableist, exclusionary, or demeaning expressions.
- Do not rely on color alone to communicate meaning.
- Provide meaningful alt text for informative images.
- Make link text understandable out of context.
- Avoid culturally specific jokes or references.

## Review mode

When asked to review documentation:

1. Identify correctness and clarity problems.
2. Check voice, tone, terminology, headings, formatting, links, procedures, and code presentation.
3. Prefer concrete replacement wording over vague criticism.
4. Preserve technically necessary terminology.
5. Do not change correct technical content merely to make it stylistically different.
6. Return a polished version when the user asks for an edit.

## Decision hierarchy

When rules conflict, use this order:

1. Project-specific requirements.
2. Product terminology and established UI names.
3. This skill.
4. General English usage.

If a deviation improves clarity for the intended audience, use it consistently and explain the exception when useful.

## Source

This skill is based on the public Google Developer Documentation Style Guide:
https://developers.google.com/style

Use the official guide as the authority when a question requires a rule that is not covered here or when the current Google guidance may have changed.
