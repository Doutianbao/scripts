// ==UserScript==
// @name         Save Tables of MDPI
// @author       Lucas Fu
// @namespace    http://tampermonkey.net/
// @version      1
// @description  Save tables with class html-table_show as HTML file
// @match        https://www.mdpi.com/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    window.addEventListener('load', function() {
        let url = window.location.href;
        fetch(url)
            .then(response => response.text())
            .then(data => {
                let parser = new DOMParser();
                let doc = parser.parseFromString(data, 'text/html');
                let tables = doc.querySelectorAll('div.html-table_show');
                if (tables.length > 0) {
                    if (confirm('Do you want to download the tables?')) {
                        let html = '<html><body>';
                        for (let table of tables) {
                            table.querySelectorAll('a').forEach(a => a.href = url + a.getAttribute('href'));
                            html += table.outerHTML;
                        }
                        html += '</body></html>';
                        let blob = new Blob([html], {type: 'text/html'});
                        let a = document.createElement('a');
                        a.href = URL.createObjectURL(blob);
                        a.download = 'tables.html';
                        a.click();
                    }
                } else {
                    alert('No tables found on this page.');
                }
            });
    });
})();
