import { useState, useEffect } from "react";
import { collection, addDoc, serverTimestamp } from "firebase/firestore";
import { Receive } from "./Receive";
import { db } from "../firebase";
import styled from "styled-components";
import LS2Request from '@enact/webos/LS2Request';

const Send = () => {
  const bridge = new LS2Request();
  const [chat, setChat] = useState("");
  const createToast = (message) => {
    bridge.send({
      service: "luna://com.webos.notification",
      method: "createToast",
      parameters: {
        message
      }
    });
  }
  useEffect(() => {
    createToast("Mode Changed!")
  }, [])


  const onSubmit = async (e) => {
    e.preventDefault();
    await addDoc(collection(db, "messages"), {
      message: chat,
      timestamp: serverTimestamp(),
      user: "host"
    });

    setChat("");
    console.log("success");
  };

  const onChange = (e) => {
    const {
      target: { value },
    } = e;
    setChat(value);
  };

  return (
    <>
      <div className="App">
        <Container>

          <Container3>
            <Container0>
              <Receive />
            </Container0>
            <iframe src="https://isekaideveloper.herokuapp.com/roo" allow="camera" title="내용" width="780px" height="360px" style={{ position: "absolute", left: "900px" }} ></iframe>
            <TextContainer>IsekaiDev</TextContainer>
          </Container3>
          <form onSubmit={onSubmit}>
            <Input>
              <input

                value={chat}
                onChange={onChange}
                type="text"
                placeholder="내용을 입력하세요..."
                maxLength={120}
              />
              <button disabled={!chat} type="submit">입력</button>
            </Input>
          </form>
        </Container>
      </div>
    </>

  );
};


const Container = styled.div`
  width: 1500px;
  height: 900px;
  background-color: #fff;
  padding: 8px;
  margin: 10px auto;
  border-radius: 5px;
  border: 1px solid #ddd;
`;
const Container0 = styled.div`
  width: 41%;
  height: 670px;
  background-color: #fff;
  padding: 16px;
 
  margin-right: 60px;
  border-radius: 5px;
  border: 1px solid #ddd;
  overflow-x: hidden;
  overflow-y: auto;
  &::-webkit-scrollbar {
    width: 20px;
  }
  &::-webkit-scrollbar-thumb {
    border-radius: 2px;
    background: #FF5C8D;
  }
`;

const Container3 = styled.div`
  width: 90%;
  height: 80%;
  background-color: #fff;
  padding: 8px;
  margin: 10px ;

  display:flex;
`;

const TextContainer = styled.h1`
    width : 780px;
    height : 380px;
    color : #fff;
    border : #524A4E;
    border-radius : 10px;
    background-color : #524A4E;
    font-size : 70px;
    margin-left : 35px;
    margin-top : 452px;
    margin-right : -200px;
    text-align : center;
    line-height : 380px;
    font-weight : bold;
  `;
const Input = styled.div`
  width: 37%;
  height: 60px;
  background-color: #fff;
  padding: 16px;
  margin-left: 18px;
  margin-right: 16px;
  margin-bottom: 60px;
  margin-top:100 px;
  
  border-radius: 5px;
  border: 1px solid #ddd;
  display: flex;
  & > *{
    padding: 5px;
  }
  & input:focus{
    outline: none;
    border: 3px solid #524A4E;
    border-radius: 10px;
  }
  & input {
    margin-right: 10px;
    width : 90%;
  }
  & button {
    width : 10%;
    color : #fff;
    border : #524A4E;
    border-radius: 10px;
    background-color: #524A4E;
  }`

export { Send }

