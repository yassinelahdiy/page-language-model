# ✍️ PLM Naming Conventions

To ensure consistency across PLM files and support smooth AI parsing and tooling, the following naming conventions are recommended.

---

## 🟢 Field Names (Keys)

Use **`camelCase`** for all structural keys and field names.

These include:
- `page`
- `url`
- `components`
- `valueBinding`
- `exampleInput`
- `llmHint`

**✅ Examples:**

```json
"id": "loginButton",
"page": "DashboardPage",
"valueBinding": "Welcome back, {{user_first_name}}",
"exampleInput": "john@example.com"
```

---

## 🐍 Enum or Action Values

Use **`snake_case`** for any string values that represent:

- Actions (`"open_modal"`, `"create_deal"`)
- Component types (`"icon_button"`, `"card_list"`)
- System or testable handlers

These are treated more like **keywords** than data.

**✅ Examples:**

```json
"type": "open_modal",
"action": "create_deal",
"variant": "mini_modal"
```

Why `snake_case`?

- It’s easier for LLMs and test agents to interpret as intent  
- It keeps action keywords visually distinct from field names

---

## 💡 Component Identifiers (`id`)

Use **`snake_case`** for component `id` values.

This improves:

- Readability
- Reusability in transitions, interactions, selectors

**✅ Examples:**

```json
"id": "create_deal_button",
"id": "sidebar_nav",
"id": "welcome_message"
```

---

## 🧠 Summary by Use Case

| Use Case               | Style        | Example                    |
|------------------------|--------------|----------------------------|
| Field names (keys)     | `camelCase`  | `valueBinding`, `llmHint`  |
| Enum/action values     | `snake_case` | `"type": "open_modal"`     |
| Component IDs          | `snake_case` | `"id": "nav_deals"`        |
| Page Names             | `PascalCase` | `"page": "DashboardPage"`  |

> 💡 **Note:** Page names and transitions use `PascalCase` to clearly distinguish full-page constructs like `"DashboardPage"` or `"DealDetailsPage"` from component IDs (`snake_case`) and enum values (`snake_case`). This helps maintain clear visual and structural separation between page-level definitions and lower-level UI elements.

---

## 🔍 Full Example

```json
{
  "id": "create_deal_modal",
  "type": "modal",
  "variant": "form_modal",
  "description": "Modal for creating a new deal",
  "fields": [
    {
      "id": "deal_name",
      "type": "input",
      "label": "Deal Name",
      "required": true
    }
  ],
  "actions": {
    "onSubmit": {
      "type": "create_deal",
      "transitionsTo": "DealDetailsPage"
    }
  }
}
```

---

## ✅ Why It Matters

These conventions:

- Make PLMs easier to **read**, **version**, and **review**
- Improve LLM performance for test generation and behavior analysis
- Keep your format future-proof and cross-platform-friendly

---

> 💡 Tip: You can add these conventions as optional soft rules in a PLM linter.
