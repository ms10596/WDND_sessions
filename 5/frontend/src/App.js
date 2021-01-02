import React, {Component} from 'react'
import './App.css';


class App extends Component {
    state = {
        "posts": []
    }

    async componentDidMount() {
        let res = await fetch("http://localhost:5000/posts")
        res = await res.json()
        this.setState({"posts": res["posts"]})
    }


    render() {
        return(
            <div>
                {this.state.posts.map(post => <div><h1>{post.id}</h1><div>{post.body}</div></div>)}
            </div>
        )
    }
  
}

export default App;
