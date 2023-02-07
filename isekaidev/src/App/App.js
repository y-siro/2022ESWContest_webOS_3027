import React from 'react';
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import { Send } from '../views/component/Send';
import {H_Send} from '../views/component/Sl2'
import styles from './mystyle.module.css'; 

function Header() {
	return(
		<>
				<Link to="/main"><img src = {require("./images/cap_home.PNG")} className = {styles.hello2}></img></Link>

		</>
	)
}	
function Main(){
	return (
		<>
			<h3 className = {styles.maintext}>수어인식 채팅 시스템</h3> 
			<ul>
			
				<Link to="/send" ><div className = {styles.hello3}>KeyBoard</div></Link>
				<Link to="/send_h" ><div className = {styles.hello4}>SignLang</div></Link>	
				
			</ul>
		</>
	);
}

const App = () => {
	return (
		<div className={styles.bigblue} >
			<BrowserRouter >
				<Header />
				<Routes >
					<Route path="/main" element={<Main />}></Route>
					<Route path="/send" element={<Send />}></Route>
					<Route path="/send_h" element={<Sl2 />}></Route>
				</Routes>
			</BrowserRouter>
		</div>
	);
};


export default App;