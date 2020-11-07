import React, {Component} from 'react'
import './App.css';


class App extends Component {

  constructor() {
    super()
    this.state = {"posts": []}
  }
  componentDidMount() {
    fetch("http://localhost:5000/posts").then(
      result => result.json().then(
        result => this.setState({"posts": result.posts})
      )
    )
  }

  render() {
    return (
      <div>
        {this.state.posts.map(post => <div><h1>{post.id}</h1><h2>{post.user_id}</h2><div>{post.body}</div></div>)}
      </div>
    )
  }
  
}

export default App;
