# How to Run Live Server

This project can be served using several methods:

## Option 1: VS Code / Cursor Live Server Extension (Recommended)

1. Install the "Live Server" extension in VS Code/Cursor:
   - Open Extensions (Ctrl+Shift+X)
   - Search for "Live Server" by Ritwick Dey
   - Click Install

2. Start the server:
   - Right-click on `index.html`
   - Select "Open with Live Server"
   - Or click the "Go Live" button in the status bar

The page will automatically reload when you make changes.

## Option 2: Python HTTP Server (Simple)

1. Make the script executable:
   ```bash
   chmod +x start-server.sh
   ```

2. Run the server:
   ```bash
   ./start-server.sh
   ```
   
   Or specify a custom port:
   ```bash
   ./start-server.sh 8080
   ```

3. Open your browser to: `http://localhost:8000`

## Option 3: Python HTTP Server (Manual)

Run this command in the project directory:
```bash
python3 -m http.server 8000
```

Then open: `http://localhost:8000`

## Option 4: Node.js http-server (If Node.js is installed)

1. Install http-server globally:
   ```bash
   npm install -g http-server
   ```

2. Run the server:
   ```bash
   http-server -p 8000
   ```

3. Open: `http://localhost:8000`

## Note

Make sure you're accessing the page through `http://localhost` (not `file://`) to avoid CORS issues with local resources.

