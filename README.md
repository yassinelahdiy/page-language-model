# 📄 Page Language Model (PLM)

**Page Language Model (PLM)** is a new open-source format for describing the structure, behavior, and flow of pages in web and mobile applications — designed specifically for **AI-assisted testing, automation, and reasoning**.

It combines the familiar **Page Object Model (POM)** with the power of **Large Language Models (LLMs)** to give intelligent agents a structured, machine-readable understanding of your app.

---

## 🔍 Why PLM?

Modern apps can be too complex to test with raw selectors and brittle flows.

PLM solves this by providing:

- 🔗 **Linked page flows** (what pages connect to what)
- 🔘 **Detailed component maps** (inputs, buttons, modals, etc.)
- ✅ **Validation and requirement rules**
- 🧠 **AI-ready format** for test generation, analysis, and understanding

It's declarative, JSON-based, and version-controlled — built for developers, testers, and LLM-powered tools.

PLMs also support rich metadata like `description`, `intent`, `exampleInput`, and `llm_hint` to help LLMs understand the role and behavior of each component.

---

## 🧠 What Does a PLM Look Like?

Here’s a basic example for a login page, using both structural fields and LLM-aware metadata:

```json
{
  "page": "LoginPage",
  "url": "/login",
  "components": [
    {
      "id": "emailInput",
      "type": "input",
      "label": "Email",
      "required": true,
      "validation": "must be a valid email",
      "exampleInput": "jon@example.com",
      "description": "User's login email address",
      "intent": "Capture the user's email for login"
    },
    {
      "id": "passwordInput",
      "type": "input",
      "label": "Password",
      "required": true,
      "validation": "minimum 8 characters",
      "exampleInput": "securepass123",
      "description": "User's password",
      "intent": "Collect secure password input"
    },
    {
      "id": "loginButton",
      "type": "button",
      "label": "Log In",
      "action": "submitLoginForm",
      "transitionsTo": "DashboardPage",
      "llm_hint": "Only enable after email and password fields are filled and valid",
      "description": "Submits login credentials and redirects on success"
    }
  ]
}
```

👉 See [`examples/login-page.json`](examples/login-page.json) for a full example.

---

## 🧱 What’s in This Repo?

- `schema/plm.schema.json` – the official v0.2 PLM JSON schema
- `examples/` – sample pages to learn from and fork
- `docs/` – deeper guides and best practices
- `cli/` – (coming soon) CLI tools for working with PLM files

---

## 🚀 Coming Soon

- CLI to validate and scaffold PLMs
- PLM → test case generators (Cypress, Playwright, etc.)
- Visual editor + LLM agent integrations

---

## ✨ Origin

PLM was created in 2025 by Jonathan Miller as a new standard to bridge the gap between UI automation, manual testing and AI reasoning.

> "Don't just test your UI — help AI understand it."

---

## 🤝 Want to Help?

- ⭐ Star the repo to follow along
- 📂 Try building your own PLM files
- 📣 Open issues or discussions
- 🧠 Spread the word and help define the standard

---

👉 See [`docs/README.md`](docs/README.md) for the full PLM spec and advanced usage.

---

## 📜 License

MIT License — free to use, modify, and build on.  
If you're interested in contributing, collaborating, or helping shape this standard, [get in touch](https://github.com/JonnyMiller99).
