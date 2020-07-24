function messageConsole(id, maxlinenum) {
    this.DocumentId = id;
    this.maxLineNum = maxlinenum;
    this.currentLineNum = 0;
    this.queueText = [];

    this.addLoggingLine = function (msg) {
        if (this.currentLineNum > this.maxLineNum) {
            this.queueText.shift()
        }
        this.currentLineNum = this.currentLineNum + 1;
        this.queueText.push(msg);
        var temptxt = "";
        for (i = 0; i < this.queueText.length; i++) {
            temptxt = temptxt + this.queueText[i] + '\n';
        }
        var txt = $(this.DocumentId);
        txt.val(temptxt)
        $(this.DocumentId).scrollTop($(this.DocumentId)[0].scrollHeight);
    }
}