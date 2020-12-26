import React from 'react'


class App extends React.Component {
  constructor() {
    super()
    this.state = {
      avatar_url: "",
      username: ""
    }
    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }
  async handleSubmit() {
    var res = await fetch("https://api.github.com/users/" + this.state.username)
    res = await res.json()
    this.setState({
      avatar_url: res.avatar_url
    })
    
  }
  handleChange(event) {
    this.setState({
      username: event.target.value
    })
  }

  
  render() {
    return (
      <div>
        <input type="text" id="username" onChange={this.handleChange}/>
        <input type="button" value="submit"  onClick={this.handleSubmit}/>
  
        <img id="img" src={this.state.avatar_url} alt="user" />
      </div>
    );
  }
  
}

export default App;
