const saveBlob = function(blob, fileName) {
    let url = URL.createObjectURL(blob);
    let link = document.createElement('a');
    link.href = url;
    link.download = fileName;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(url);
};

const initializeEditor = function (editor) {
    editor.setTheme("ace/theme/monokai");
    editor.session.setMode("ace/mode/python");
    editor.setOptions({
        fontSize: '12pt',
        enableBasicAutocompletion: true,
        enableLiveAutocompletion: true,
        showPrintMargin: false,
    })
};

let editor = ace.edit("editor");
let console = document.getElementById("console");
let editorRun = document.getElementById('editor-run');
let editorSave = document.getElementById('editor-save');
let editorReset = document.getElementById('editor-reset');

initializeEditor(editor);

editorReset.addEventListener('click', () => {
    editor.setValue('');
});

editorSave.addEventListener('click', () => {
    let textContent = editor.getValue();
    let blob = new Blob([textContent], { type: 'text/plain' });
    saveBlob(blob, 'main.py');
});