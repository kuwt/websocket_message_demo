/********
   message window
   **********/
var maxLineNum = 10;
var currentLineNum = 0;
var queueText = [];
var messageConsoleDocumentId;

function appendLineToTextArea(s) {
    if (currentLineNum > maxLineNum) {
        queueText.shift()
    }
    currentLineNum = currentLineNum + 1;
    queueText.push(s);
    var temptxt = "";
    for (i = 0; i < queueText.length; i++) {
        temptxt = temptxt + queueText[i] + '\n';
    }
    var txt = $(messageConsoleDocumentId);
    txt.val(temptxt)
    $(messageConsoleDocumentId).scrollTop($(messageConsoleDocumentId)[0].scrollHeight);
}

function setActiveMessageConsole(id) {
    messageConsoleDocumentId = id;
}