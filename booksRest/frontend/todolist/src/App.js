import logo from './logo.svg';
import './App.css';
import {Form} from './form'
import { toHaveStyle } from '@testing-library/jest-dom/matchers';

function App() {
  return (
    <div className="App">
      <h1>Yika Todos</h1>
      <div className='todo-wrapper'>
        <div className='todo-input'>
          <div className='todo-input-item'>
            <label>Title</label>
            <input type='text' placeholder='enter a title'/>
          </div>
          <div className='todo-input-item'>
            <label>Description</label>
            <input type='text' placeholder='enter a description'/>
          </div>
          <div className='todo-input-item'>
            <button className='primaryBtn'>Add</button>
          </div>
        </div>
        <div className='btn-area'>
          <button className='btnitem'>Todo</button>
          <button className='btnitem'>Completed</button>
        </div>
        <div className='todo-list'>
          <div className='todo-list-item'>
            <h1>Task 1</h1>
            <p>description</p>
          </div>
        </div>
      </div>
      <Form/>
    </div>
  );
}

export default App;
