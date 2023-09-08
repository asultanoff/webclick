document.getElementById('submit').addEventListener('click', function() {
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
        var activeTab = tabs[0];
        var selectedChoice = document.getElementById('choice').value;
        chrome.tabs.sendMessage(activeTab.id, {"message": "submit", "choice": selectedChoice});
    });
});
