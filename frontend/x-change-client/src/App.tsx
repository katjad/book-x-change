import React from 'react';
import logo from './logo.svg';
import './App.css';

const App: React.FC = () => {
    return (
        <div className="App">
            <header className="App-header">
                <img src={logo} className="App-logo" alt="logo" />
                <p>
                    <strong>x-change-client</strong>
                </p>
                <p>
                    Run 'yarn storybook' to see a demo for semantic-ui-react Button
                </p>
            </header>
        </div>
    );
}

export default App;
