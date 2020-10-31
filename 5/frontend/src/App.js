import './App.css';
import React, {Component} from 'react'

class App extends Component {

  constructor() {
    super()
    this.state = {
      "posts": []
    }
  }
  componentDidMount() {
    fetch("http://localhost:5000/posts").then(
      res => res.json().then(
        res => this.setState({"posts": res.posts})
      )
    )
  }
  
  render() {
    return (
      <div>
        {this.state.posts.map(post => <div><h1>{post.id}</h1><span>{post.body}</span></div>)}
      </div>
    );
  }
  
}

export default App;
