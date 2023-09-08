# Web Click Action Recorder

## Description
This app captures the `outerHTML` of any element clicked by the user on any webpage, then prompts the user to select or create an action associated with the clicked element, and finally saves the URL, `outerHTML`, and selected action to a CSV file.

The app consists of a browser extension that captures the `outerHTML` of the clicked element and sends it to a Python WebSocket server, and a Python script that receives the messages from the WebSocket server, prompts the user to select or create an action, and saves the data to a CSV file.

## Installation

1. Install the required Python packages by running:
```
pip install websockets pandas
```

2. Install the browser extension:

    a. Load the `extension` folder as an unpacked extension in your browser.

    b. Update the `manifest.json` file to include the necessary permissions for your use case.

3. Run the Python script by running:
```
python app.py
```

## Usage

1. Run the Python script.

2. Load the browser extension.

3. Open a webpage and start clicking on elements. The `outerHTML` of the clicked element and the current URL will be captured by the browser extension and sent to the Python WebSocket server.

4. For each received message, a popup window will appear, prompting you to select or create an action associated with the clicked element. You can select an existing action from the list, or create a new action by entering it in the text box and clicking 'OK'.

5. The URL, `outerHTML`, and selected action will be saved to a CSV file named `data.csv` in the same directory as the Python script.

## License

This project is licensed under the MIT License.

***

You can customize the README file according to your needs. Make sure to include any additional information that is necessary for your app.
