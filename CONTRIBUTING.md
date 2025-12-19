Contribution Guidelines
=======================

Thank you for your interest in contributing to the Driver Drowsiness Detection System. To maintain a professional and efficient development environment, please adhere to the following guidelines.

Reporting Issues
----------------
- Use the provided Issue Templates for bug reports or feature requests.
- Provide a clear and descriptive title.
- Include steps to reproduce bugs and relevant technical environment details.

Development Process
-------------------
1. Fork the repository and create your branch from `main`.
2. Ensure your code follows the existing modular architecture.
3. Include docstrings for all new functions and classes (Google Style).
4. Remove any casual elements such as emojis or informal logging.
5. Verify your changes by running the automated test suite:
   ```bash
   python3 -m unittest discover tests
   ```

Submission Standards
--------------------
- All pull requests will be automatically validated via the CI pipeline.
- Ensure that the `README.md` and `walkthrough.md` are updated if new features are introduced.
- Maintain the Setext-style header format (underlines) for all documentation.

By contributing, you agree that your contributions will be licensed under the project's MIT License.
