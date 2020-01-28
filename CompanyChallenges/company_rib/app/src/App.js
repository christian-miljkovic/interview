import React from 'react';
import logo from './logo.svg';
import './App.css';

class App extends React.Component {

  constructor(props){
    super(props);
    this.startPlaid = this.startPlaid.bind(this);
    this.onSuccess = this.onSuccess.bind(this);
    this.state = {banks:[]};
  }

  render(){
    var banks = this.state.banks.map((bank) => 
      <li>{bank}</li> 
    );

    return (
      <div className="App">
  
        <button id="link-button" onClick={this.startPlaid}>Link Account</button>
        {banks}
        
      </div>
    );
  }

  startPlaid(){
    var Plaid = window.Plaid;

    var handler = Plaid.create({
      clientName: 'Plaid Quickstart',
      // Optional, specify an array of ISO-3166-1 alpha-2 country
      // codes to initialize Link; European countries will have GDPR
      // consent panel
      countryCodes: ['US'],
      env: 'sandbox',
      // Replace with your public_key from the Dashboard
      key: 'f0a6f0f94e276e99db08a7e06fc75a',
      product: ['transactions'],
      // Optional, use webhooks to get transaction and error updates
      webhook: 'https://requestb.in',
      // Optional, specify a language to localize Link
      language: 'en',
      // Optional, specify userLegalName and userEmailAddress to
      // enable all Auth features
      userLegalName: 'John Appleseed',
      userEmailAddress: 'jappleseed@yourapp.com',
      onLoad: function() {
        // Optional, called when Link loads
      },
      onSuccess: this.onSuccess,
      onExit: function(err, metadata) {
        // The user exited the Link flow.
        if (err != null) {
          // The user encountered a Plaid API error prior to exiting.
        }
        // metadata contains information about the institution
        // that the user selected and the most recent API request IDs.
        // Storing this information can be helpful for support.
      },
      onEvent: function(eventName, metadata) {
        // Optionally capture Link flow events, streamed through
        // this callback as your users connect an Item to Plaid.
        // For example:
        // eventName = "TRANSITION_VIEW"
        // metadata  = {
        //   link_session_id: "123-abc",
        //   mfa_type:        "questions",
        //   timestamp:       "2017-09-14T14:42:19.350Z",
        //   view_name:       "MFA",
        // }
      }
    })
  
    handler.open()

  }

  onSuccess(public_token, metadata){
    let banks = this.state.banks;
    banks.push(metadata.institution.name);

    this.setState({banks:banks});
  }

  }
  



export default App;
