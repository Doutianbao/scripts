# 让我一个一个复制粘贴再编辑是不可能的，这辈子也不可能的 #

*暂时只适配https://www.mdpi.com/* 

*感谢new bing*


save_tables.py
---

需要电脑提前安装python3，然后运行即可，会自动安装额外需要的packages


save_tables.js
---

适用于电脑浏览器（chrome，火狐，edge等），部分手机浏览器也可以，比如wiki浏览器
浏览器需要安装tampermonkey插件，其他类似插件也可以：》


RESPECT!
---
MD2excel.py
# Markdown Table to Excel Converter

This project provides a simple GUI application for converting Markdown tables into Excel files. The application is built using Python, with dependencies on `pandas`, `openpyxl`, and `tkinter`.

## Features

- **Markdown to Excel Conversion:** Easily convert Markdown table data into an Excel file.
- **User-Friendly Interface:** Simple GUI for inputting Markdown table data and saving the output file.
- **Automatic Dependency Installation:** Checks and installs missing dependencies automatically.

## Installation

To run this application, you need Python installed on your system. The required Python packages will be installed automatically when you run the script.

### Required Packages

- `pandas`
- `openpyxl`
- `tkinter`

## Usage

1. **Clone the Repository:** (If applicable)
   ```
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Script:**
   ```bash
   python markdown_to_excel.py
   ```

3. **Input Markdown Table:**
   - Enter your Markdown table data into the text input area.

4. **Convert to Excel:**
   - Click the "转换为Excel" button to convert the Markdown table to an Excel file.
   - Choose the save location for the Excel file via the file dialog that appears.

5. **Save the File:**
   - The Excel file will be saved at the specified location, and a success message will be displayed.

## Example

### Input (Markdown Table):

```
| Name    | Age | Occupation  |
|---------|-----|-------------|
| John    | 30  | Engineer    |
| Alice   | 28  | Doctor      |
| Michael | 35  | Artist      |
```

### Output (Excel File):

An Excel file with columns "Name", "Age", "Occupation" and corresponding data.

## Code Overview

- **Dependency Check and Installation:**
  The script checks for the required packages and installs them if they are missing.

- **Main Functionality:**
  - `markdown_to_excel`: Reads the Markdown table from the text input, converts it to a pandas DataFrame, and saves it as an Excel file.

- **GUI Components:**
  - A simple GUI using `tkinter` that includes:
    - A text input area for the Markdown table.
    - A button to trigger the conversion.
    - A label to display the result status.

## Notes

- Ensure you have an active internet connection for the first-time dependency installation.
- The `tkinter` package is included with most Python installations, but if you're using a custom Python environment, you may need to install it separately.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any changes or suggestions.

## Acknowledgements

This project uses the following open-source packages:
- [pandas](https://pandas.pydata.org/)
- [openpyxl](https://openpyxl.readthedocs.io/)
- [tkinter](https://docs.python.org/3/library/tkinter.html) (part of the Python standard library)
