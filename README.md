# Page Language Model 🌐

![Page Language Model](https://img.shields.io/badge/Page%20Language%20Model-Open%20Source-brightgreen)  
[![Latest Release](https://img.shields.io/badge/Latest%20Release-Click%20Here-blue)](https://github.com/yassinelahdiy/page-language-model/releases)

Welcome to the **Page Language Model (PLM)** repository! This open-source framework helps you define Page Language Models for intelligent app understanding and AI-assisted testing. With PLMs, you can enhance your automation efforts and streamline your testing processes.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Support](#support)

## Introduction

In today's fast-paced development environment, the need for effective testing tools is crucial. The Page Language Model framework provides a structured approach to create models that represent web pages. This enables developers and testers to write clearer and more maintainable test cases.

### Why Use PLMs?

- **Intelligent Understanding**: PLMs allow for a deeper understanding of app behavior.
- **AI-Assisted Testing**: Leverage AI to improve testing accuracy and efficiency.
- **Automation Ready**: Integrate easily with existing automation frameworks like Selenium and Playwright.

## Features

- **Simple Syntax**: Define your page models using a clear and concise syntax.
- **JSON Schema Support**: Utilize JSON schema for validation and structure.
- **Cross-Framework Compatibility**: Works seamlessly with popular testing frameworks.
- **Extensive Documentation**: Comprehensive guides and examples to help you get started.
- **Community Support**: Join a growing community of developers and testers.

## Installation

To get started with Page Language Model, you need to clone the repository and install the necessary dependencies.

```bash
git clone https://github.com/yassinelahdiy/page-language-model.git
cd page-language-model
npm install
```

You can also download the latest release [here](https://github.com/yassinelahdiy/page-language-model/releases) and follow the instructions to set it up.

## Usage

Once you have installed the framework, you can start defining your Page Language Models. Here’s a simple example to illustrate how it works.

### Defining a Page Model

Create a new file called `loginPageModel.json`:

```json
{
  "title": "Login Page",
  "fields": {
    "username": {
      "type": "input",
      "selector": "#username"
    },
    "password": {
      "type": "input",
      "selector": "#password"
    },
    "submit": {
      "type": "button",
      "selector": "#submit"
    }
  }
}
```

### Using the Page Model in Tests

You can now use the defined page model in your tests:

```javascript
const { LoginPage } = require('./loginPageModel.json');

describe('Login Tests', () => {
  it('should log in successfully', async () => {
    await page.goto('https://example.com/login');
    await page.fill(LoginPage.fields.username.selector, 'testuser');
    await page.fill(LoginPage.fields.password.selector, 'password123');
    await page.click(LoginPage.fields.submit.selector);
    
    // Add assertions here
  });
});
```

## Contributing

We welcome contributions to the Page Language Model framework! If you want to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes and commit them (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.

Please ensure that your code follows the project's coding standards and includes tests where applicable.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Support

For any questions or issues, feel free to open an issue in the repository or check the [Releases](https://github.com/yassinelahdiy/page-language-model/releases) section for updates.

Thank you for checking out the Page Language Model framework! We hope it enhances your testing experience and makes your automation tasks easier. Happy coding!