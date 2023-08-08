// declare sheet
var ss = SpreadsheetApp.getActiveSpreadsheet();
var mainSheet = ss.getSheetByName('Dettaglio Operatore')
// declare API
var API_URL = 'https://r6s-api.onrender.com/operator?operator='
// pick up operator argument
//var operator = mainSheet.getRange(1, 2).getValue().toString().toLowerCase()

// define empty array
var keys = []
var values = []


// clear sheet
mainSheet.getRange("A2:B16").clearContent()

function onOpen() {
  SpreadsheetApp.getUi() // Or DocumentApp or SlidesApp or FormApp.
    .createMenu('Custom Menu')
    .addItem('Show prompt', 'showPrompt')
    .addToUi();
}

function showPrompt() {
  var ui = SpreadsheetApp.getUi(); // Same variations.

  var result = ui.prompt(
    'Please enter the name of operator',
    'Click OK and change sheet to view the result',
    ui.ButtonSet.OK_CANCEL
    );

  // Process the user's response.
  var button = result.getSelectedButton();
  var text = result.getResponseText();
  if (button == ui.Button.OK) {
    text = text.toLowerCase()
    text = text.trim()
    pullData(text)
  } else if (button == ui.Button.CANCEL) {

    ui.alert('I didn\'t get the name.');
  } else if (button == ui.Button.CLOSE) {

    ui.alert('You closed the dialog.');
  }
}

// define function
function pullData(operator) {
  var URL = API_URL + operator; // concat API + operator
  Logger.log("Sending GET request to: " + URL)
  var response = UrlFetchApp.fetch(URL); // call api 

  if (response.getResponseCode() == 200) {
    if (response.lenght != 0) {
      var jsonContent = JSON.parse(response.getContentText());

      // inizio brutto
      var r6s_info_key = Object.keys(jsonContent[0])
      var r6s_info_value = Object.values(jsonContent[0])

      var loudout_key = Object.keys(jsonContent[1])
      var loudout_value = Object.values(jsonContent[1])

      var bio_info_key = Object.keys(jsonContent[2])
      var bio_info_value = Object.values(jsonContent[2])

      var biography_key = Object.keys(jsonContent[3])
      var biography_value = Object.values(jsonContent[3])

      keys = r6s_info_key.concat(loudout_key, bio_info_key, biography_key)
      values = r6s_info_value.concat(loudout_value, bio_info_value, biography_value)
      // fine brutto

      for (i = 0; i < keys.length; i++) {
        Logger.log("Starting write on sheet " + mainSheet.getName() + ' ' + keys[i])

        row = 2 + i
        mainSheet.getRange(1, 1).setValue(operator)
        mainSheet.getRange(row, 1).setValue(keys[i])
        mainSheet.getRange(row, 2).setValue(values[i])
        SpreadsheetApp.flush()
      }
    } else {
      mainSheet.getRange(2, 2).setValue('JSON empty')
    }
  } else {
    mainSheet.getRange(2, 2).setValues('Error ' + response.getResponseCode(), response.getContent())
  }

}

