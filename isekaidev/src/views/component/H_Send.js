
import React, { useEffect, useState } from "react";
import { H_Receive } from "./H_Receive";
import styled from "styled-components";
import LS2Request from "@enact/webos/LS2Request";

const H_Send = () => {
    const bridge = new LS2Request();
    const [text, setText] = useState("START");
    const [text2, setText2] = useState("IsekaiDev");
    const [bool, setBool] = useState(false);    

    let flag = 0;
    let params = {};
    function get_set() {
        console.log("__in get set__");
        var Request = {
            service: "luna://com.sl.app.service",
            method: "startScreenshot",
            parameters: params,
            onSuccess: (msg) => {
                console.log(msg);
            },
            onFailure: (err) => {
                console.log(err);
            },
        };
        bridge.send(Request);
    }

    function stop() {
        var Request = {
            service: "luna://com.sl.app.service",
            method: "stopScreenshot",
            parameters: params,
            onSuccess: (msg) => { console.log(msg); },
            onFailure: (err) => { console.log(err); },
        };
        bridge.send(Request);
    }

    useEffect(() => {
        console.log("set camera");
        var Request = {
            service: "luna://com.sl.app.service",
            method: "setService",
            parameters: params,
            onSuccess: (msg) => { console.log(msg); },
            onFailure: (err) => { console.log(err); },
        };
        bridge.send(Request);
    }, []);

    const onToggle = (e) => {
        if (bool) {
            setText("START");
            setText2("IsekaiDev");
            setBool(false);
            stop();
        }
        else {
            setText("END");
            setText2("잠시만 기다려주세요...");
            setBool(true);
            get_set();
        }
    }

    return (
        <>
            <div className="App">
                <Container>

                    <Container3>
                        <Container0>
                            <H_Receive />
                        </Container0>

                        <iframe src="https://isekaideveloper.herokuapp.com/roo" allow="camera" title="내용" width="780px" height="360px" style={{ position: "absolute", left: "900px" }} ></iframe>
                        <TextContainer>{text2}</TextContainer>
                    </Container3>
                    <BTN>
                        <button onClick={onToggle}>{text}</button>
                    </BTN>

                </Container>
            </div>
        </>
    );
};

export { H_Send };

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
    width : 640px;
    height : 350px;
    color : #fff;
    border : #524A4E;
    border-radius: 10px;
    background-color: #524A4E;
    font-size: 55px;
    font-weight : bold;
    margin-left: 35px;
    margin-top : 452px;
    margin-right: -200px;
    text-align:center;
    line-height:350px;
  `;

const BTN = styled.div`
   button {
    width : 39%;
    height : 60px;
    margin-left:18px;
    color : #fff;
    border : #524A4E;
    border-radius: 10px;
    background-color: #524A4E;
    font-weight: bold;
    font-size : 40px;
  }`