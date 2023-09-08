var ws = new WebSocket('ws://localhost:5000');
ws.onopen = function(event) {
    document.addEventListener('click', function(e) {
        var data = {
            url: window.location.href,
            outerHTML: e.target.outerHTML
        }
        ws.send(JSON.stringify(data));
    });
};
ws.onerror = function(error) {
    console.error('WebSocket error:', error);
};
ws.onclose = function(event) {
    console.log('WebSocket connection closed:', event);
};
