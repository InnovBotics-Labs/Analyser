# Budget Analyser UML Diagrams

This directory contains UML diagrams for the Budget Analyser application.

## Class Diagram

The `class_diagram.puml` file contains a PlantUML definition of the class structure of the Budget Analyser application. It shows:

- The main classes in the application
- Their attributes and methods
- The relationships between classes
- The package organization

### Prerequisites

Before you can generate UML diagrams with PlantUML, you need to install Graphviz:

#### Installing Graphviz

PlantUML requires Graphviz to generate diagrams. If you encounter the error "Dot executable doesn't exist can't find graphviz", you need to install Graphviz:

1. **Windows**:
   - Download the installer from [Graphviz Download Page](https://graphviz.org/download/)
   - Run the installer and follow the instructions
   - Add the Graphviz bin directory to your PATH environment variable

2. **macOS**:
   - Using Homebrew: `brew install graphviz`
   - Using MacPorts: `sudo port install graphviz`

3. **Linux**:
   - Ubuntu/Debian: `sudo apt-get install graphviz`
   - Fedora/RHEL/CentOS: `sudo dnf install graphviz` or `sudo yum install graphviz`
   - Arch Linux: `sudo pacman -S graphviz`

4. **Verify Installation**:
   - Open a terminal/command prompt
   - Run `dot -v` or `which dot`
   - If installed correctly, you should see version information or the path to the dot executable

### How to Generate the Visual Diagram

Once Graphviz is installed, you can generate a visual diagram from the PlantUML file using one of the following methods:

1. **Online PlantUML Server**:
   - Visit [PlantUML Server](https://www.plantuml.com/plantuml/uml/)
   - Copy and paste the content of `class_diagram.puml` into the text area
   - The diagram will be generated automatically

2. **Using PlantUML locally**:
   - Install PlantUML (requires Java): [PlantUML Installation](https://plantuml.com/starting)
   - Run the command: `java -jar plantuml.jar class_diagram.puml`
   - This will generate a PNG image in the same directory

3. **Using an IDE Plugin**:
   - Many IDEs (IntelliJ, VS Code, etc.) have PlantUML plugins
   - Install the plugin and open the `.puml` file to view the diagram

### Diagram Overview

The class diagram shows the following components:

#### View Layer
- `Ui_Widget`: The login screen UI
- `Ui_MainWindow`: The main dashboard UI
- `InputDisplayApp` and `ExpenseReport`: Test UI components

#### Model Layer
- `Statements`: Collects and formats financial transaction data
- `OriginalStatement`: Provides raw transaction data
- `StatementFormatter`: Formats raw statements into a consistent format

#### Controller Layer
- `Report`: Generates various financial reports from transaction data
- `Processor`: Processes raw transactions by adding categorization

#### Framework Layer
- `Logger`: Provides centralized logging (implemented as a Singleton)
- `PandasToolkit`: Utility methods for pandas DataFrame operations
- `JsonHandler`: Handles JSON file loading and parsing

The main application flow starts in `main_be.py`, which creates instances of `Statements`, `Processor`, and `Report` to process financial data and generate reports.

### Troubleshooting

If you encounter issues with PlantUML or Graphviz:

1. **Verify Graphviz Installation**:
   ```
   dot -v
   ```
   This should display the version of Graphviz if properly installed.

2. **Check PlantUML Configuration**:
   - Make sure PlantUML can find the Graphviz executable
   - Some IDEs require additional configuration to point to the Graphviz installation

3. **Common Issues**:
   - **"Dot executable doesn't exist can't find graphviz"**: Install Graphviz as described above
   - **Path issues**: Ensure Graphviz is in your system PATH
   - **Permission issues**: Make sure you have the necessary permissions to execute the dot command

4. **Alternative Approach**:
   - If you continue to have issues with local installation, use the online PlantUML server option
   - The online server has Graphviz pre-installed and will work without local dependencies