# 📚 PLM Docs

Welcome to the documentation for the **Page Language Model (PLM)** project.

PLM is an open-source format for describing the structure, behavior, and user flows of web/mobile applications — designed specifically for **AI-assisted testing, reasoning, and automation**.

---

## 🧱 What Is a PLM?

A **Page Language Model (PLM)** is a JSON-based definition of a page in your app. It includes:

- The page’s **identity** (name, route, description)
- The **components** on the page (inputs, buttons, links, forms, etc.)
- The **interactions** users can perform (clicks, form submits, state transitions)
- Optional **flow logic** (what happens next, what conditions apply)
- **Contextual metadata** that helps AI understand intent, purpose, and behavior

PLMs are meant to be machine-readable, human-friendly, and easily version-controlled.

---

## 🛠 PLM Structure Overview

A typical PLM file includes the following structure:

- **`page`** – the name of the page or view
- **`url`** – the route or pattern for this page (optional)
- **`components`** – an array of structured elements on the page
- **Each component** can include:
  - `id`: unique identifier
  - `type`: input, button, link, modal, etc.
  - `label`, `icon`, or `valueBinding`
  - `interactions`: user-driven actions (`onInput`, `onClick`, etc.)
  - `action`: what happens when the component is triggered
  - `validation`: requirements or conditions
  - `transitionsTo`: what page comes next (optional)

> 💡 **Note:** The PLM format is intentionally flexible and LLM-friendly.  
> You can include additional fields or structures not listed here if they help convey intent, behavior, or context.  
> LLMs are expected to semantically interpret these fields, even if they're non-standard.  
> This allows PLMs to be plug-and-play across a variety of app types and testing workflows.

---

## 🧠 Metadata for LLMs

PLMs can include **rich contextual metadata** to help large language models (LLMs) reason about components, test cases, and flows more effectively.

Supported metadata fields include:

| Field             | Purpose                                                                 |
|------------------|-------------------------------------------------------------------------|
| `description`     | Free-form explanation of the component’s purpose                       |
| `intent`          | A short summary of the user goal (e.g., "Search for an account by ID") |
| `exampleInput`    | Example value a user might enter                                       |
| `llmHint`         | Specific guidance for LLMs (e.g., "Only enable if field is numeric")    |
| `displayCondition` | When/why this component should appear                                |
| `binding` / `valueBinding` | Dynamic values sourced from app state or context             |

These fields are optional, but recommended for any PLMs intended for intelligent automation, AI-generated testing, or dynamic flow analysis.

---

## 📄 Example

See [`examples/login-page.json`](../examples/login-page.json) for a complete example of a PLM definition for a login page, including input validation, form submission, and transition logic.

---

## 🚀 Coming Soon in `docs/`

- How to write your first PLM
- Validating PLM files using the schema
- Converting a Page Object Model (POM) into a PLM
- Using PLMs to generate tests and simulate flows

---

Have ideas, questions, or contributions?  
Open an issue or jump into [Discussions](../../discussions) and help shape the PLM standard!
