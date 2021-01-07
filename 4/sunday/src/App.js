
import React from 'react'

class App extends React.Component {
  state = {
    "avatar_url": "",
    "username": ""
  }
  constructor() {
    super()
    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }
  
  async handleSubmit() {
    var result = await fetch("https://api.github.com/users/" + this.state.username)
    result = await result.json()

    this.setState({
      "avatar_url": result.avatar_url
    })
  }
  handleChange(event) {
    this.setState({
      "username": event.target.value
    })
  }
  render() {
    return (
      <div>
       <h1>Hello</h1>
      <input type="text" id="username" onChange={this.handleChange}/>
      <input type="button" value="submit" onClick={this.handleSubmit} />
  
      <img src={this.state.avatar_url} id="img" alt="username"/>
      </div>
    );
  }
  
}

export default App;
