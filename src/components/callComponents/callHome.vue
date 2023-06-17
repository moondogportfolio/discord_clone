<template>
  <p>UGAAAAAAAAAAAH</p>
  <div>
    <h1>
      <a href="//webrtc.github.io/samples/" title="WebRTC samples homepage"
        >WebRTC samples</a
      >
      <span>Peer connection: audio only</span>
    </h1>
    <div id="audio">
      <div>
        <div class="label">Remote audio:</div>
        <audio id="audio2" autoplay controls></audio>
      </div>
    </div>
    <div id="buttons">
      <select id="codec">
        <!-- Codec values are matched with how they appear in the SDP.
            For instance, opus matches opus/48000/2 in Chrome, and ISAC/16000
            matches 16K iSAC (but not 32K iSAC). -->
        <option value="opus">Opus</option>
        <option value="ISAC">iSAC 16K</option>
        <option value="G722">G722</option>
        <option value="PCMU">PCMU</option>
        <option value="red">RED</option>
      </select>
      <select id="codecPreferences" disabled>
        <option selected value="">Default</option>
      </select>
      <button id="callButton">Call</button>
      <button id="hangupButton">Hang Up</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "CallHome",
  mounted() {
    console.log("FUCK");

    const audio2 = document.querySelector("audio#audio2");
    const callButton = document.querySelector("button#callButton");
    const hangupButton = document.querySelector("button#hangupButton");
    const codecSelector = document.querySelector("select#codec");
    hangupButton.disabled = true;
    callButton.onclick = call;
    hangupButton.onclick = hangup;

    let pc1;
    let pc2;
    let localStream;

    // let bitrateGraph;
    // let bitrateSeries;
    // let headerrateSeries;

    // let packetGraph;
    // let packetSeries;

    // let lastResult;

    const offerOptions = {
      offerToReceiveAudio: 1,
      offerToReceiveVideo: 0,
      voiceActivityDetection: false,
    };

    // const audioLevels = [];
    // let audioLevelGraph;
    // let audioLevelSeries;

    // Enabling opus DTX is an expert option without GUI.
    // eslint-disable-next-line prefer-const
    let useDtx = false;

    // Disabling Opus FEC is an expert option without GUI.
    // eslint-disable-next-line prefer-const
    let useFec = true;

    // We only show one way of doing this.
    const codecPreferences = document.querySelector("#codecPreferences");
    const supportsSetCodecPreferences =
      window.RTCRtpTransceiver &&
      "setCodecPreferences" in window.RTCRtpTransceiver.prototype;
    if (supportsSetCodecPreferences) {
      codecSelector.style.display = "none";

      const { codecs } = RTCRtpSender.getCapabilities("audio");
      codecs.forEach((codec) => {
        if (["audio/CN", "audio/telephone-event"].includes(codec.mimeType)) {
          return;
        }
        const option = document.createElement("option");
        option.value = (
          codec.mimeType +
          " " +
          codec.clockRate +
          " " +
          (codec.sdpFmtpLine || "")
        ).trim();
        option.innerText = option.value;
        codecPreferences.appendChild(option);
      });
      codecPreferences.disabled = false;
    } else {
      codecPreferences.style.display = "none";
    }

    // Change the ptime. For opus supported values are [10, 20, 40, 60].
    // Expert option without GUI.
    // eslint-disable-next-line no-unused-vars
    async function setPtime(ptime) {
      const offer = await pc1.createOffer();
      await pc1.setLocalDescription(offer);
      const desc = pc1.remoteDescription;
      if (desc.sdp.indexOf("a=ptime:") !== -1) {
        desc.sdp = desc.sdp.replace(/a=ptime:.*/, "a=ptime:" + ptime);
      } else {
        desc.sdp += "a=ptime:" + ptime + "\r\n";
      }
      await pc1.setRemoteDescription(desc);
    }

    function gotStream(stream) {
      hangupButton.disabled = false;
      console.log("Received local stream");
      localStream = stream;
      const audioTracks = localStream.getAudioTracks();
      if (audioTracks.length > 0) {
        console.log(`Using Audio device: ${audioTracks[0].label}`);
      }
      localStream
        .getTracks()
        .forEach((track) => pc1.addTrack(track, localStream));
      console.log("Adding Local Stream to peer connection");

      if (supportsSetCodecPreferences) {
        const preferredCodec =
          codecPreferences.options[codecPreferences.selectedIndex];
        if (preferredCodec.value !== "") {
          const [mimeType, clockRate, sdpFmtpLine] =
            preferredCodec.value.split(" ");
          const { codecs } = RTCRtpSender.getCapabilities("audio");
          console.log(mimeType, clockRate, sdpFmtpLine);
          console.log(JSON.stringify(codecs, null, " "));
          const selectedCodecIndex = codecs.findIndex(
            (c) =>
              c.mimeType === mimeType &&
              c.clockRate === parseInt(clockRate, 10) &&
              c.sdpFmtpLine === sdpFmtpLine
          );
          const selectedCodec = codecs[selectedCodecIndex];
          codecs.splice(selectedCodecIndex, 1);
          codecs.unshift(selectedCodec);
          const transceiver = pc1
            .getTransceivers()
            .find(
              (t) =>
                t.sender && t.sender.track === localStream.getAudioTracks()[0]
            );
          transceiver.setCodecPreferences(codecs);
          console.log("Preferred video codec", selectedCodec);
        }
      }

      pc1
        .createOffer(offerOptions)
        .then(gotDescription1, onCreateSessionDescriptionError);
    }

    function onCreateSessionDescriptionError(error) {
      console.log(`Failed to create session description: ${error.toString()}`);
    }

    function call() {
      callButton.disabled = true;
      codecSelector.disabled = true;
      console.log("Starting call");
      const servers = null;
      pc1 = new RTCPeerConnection(servers);
      console.log("Created local peer connection object pc1");
      pc1.onicecandidate = (e) => onIceCandidate(pc1, e);
      pc2 = new RTCPeerConnection(servers);
      console.log("Created remote peer connection object pc2");
      pc2.onicecandidate = (e) => onIceCandidate(pc2, e);
      pc2.ontrack = gotRemoteStream;
      console.log("Requesting local stream");
      navigator.mediaDevices
        .getUserMedia({
          audio: true,
          video: false,
        })
        .then(gotStream)
        .catch((e) => {
          alert(`getUserMedia() error: ${e.name}`);
        });
    }

    function gotDescription1(desc) {
      console.log(`Offer from pc1\n${desc.sdp}`);
      pc1.setLocalDescription(desc).then(() => {
        if (!supportsSetCodecPreferences) {
          desc.sdp = forceChosenAudioCodec(desc.sdp);
        }
        pc2.setRemoteDescription(desc).then(() => {
          return pc2
            .createAnswer()
            .then(gotDescription2, onCreateSessionDescriptionError);
        }, onSetSessionDescriptionError);
      }, onSetSessionDescriptionError);
    }

    function gotDescription2(desc) {
      console.log(`Answer from pc2\n${desc.sdp}`);
      pc2.setLocalDescription(desc).then(() => {
        if (!supportsSetCodecPreferences) {
          desc.sdp = forceChosenAudioCodec(desc.sdp);
        }
        if (useDtx) {
          desc.sdp = desc.sdp.replace(
            "useinbandfec=1",
            "useinbandfec=1;usedtx=1"
          );
        }
        if (!useFec) {
          desc.sdp = desc.sdp.replace("useinbandfec=1", "useinbandfec=0");
        }
        pc1
          .setRemoteDescription(desc)
          .then(() => {}, onSetSessionDescriptionError);
      }, onSetSessionDescriptionError);
    }

    function hangup() {
      console.log("Ending call");
      localStream.getTracks().forEach((track) => track.stop());
      pc1.close();
      pc2.close();
      pc1 = null;
      pc2 = null;
      hangupButton.disabled = true;
      callButton.disabled = false;
      codecSelector.disabled = false;
    }

    function gotRemoteStream(e) {
      if (audio2.srcObject !== e.streams[0]) {
        audio2.srcObject = e.streams[0];
        console.log("Received remote stream");
      }
    }

    function getOtherPc(pc) {
      return pc === pc1 ? pc2 : pc1;
    }

    function getName(pc) {
      return pc === pc1 ? "pc1" : "pc2";
    }

    function onIceCandidate(pc, event) {
      getOtherPc(pc)
        .addIceCandidate(event.candidate)
        .then(
          () => onAddIceCandidateSuccess(pc),
          (err) => onAddIceCandidateError(pc, err)
        );
      console.log(
        `${getName(pc)} ICE candidate:\n${
          event.candidate ? event.candidate.candidate : "(null)"
        }`
      );
    }

    function onAddIceCandidateSuccess() {
      console.log("AddIceCandidate success.");
    }

    function onAddIceCandidateError(error) {
      console.log(`Failed to add ICE Candidate: ${error.toString()}`);
    }

    function onSetSessionDescriptionError(error) {
      console.log(`Failed to set session description: ${error.toString()}`);
    }

    function forceChosenAudioCodec(sdp) {
      return maybePreferCodec(sdp, "audio", "send", codecSelector.value);
    }
    function maybePreferCodec(sdp, type, dir, codec) {
      const str = `${type} ${dir} codec`;
      if (codec === "") {
        console.log(`No preference on ${str}.`);
        return sdp;
      }

      console.log(`Prefer ${str}: ${codec}`);

      const sdpLines = sdp.split("\r\n");

      // Search for m line.
      //   const mLineIndex = findLine(sdpLines, 'm=', type);
      //   if (mLineIndex === null) {
      //     return sdp;
      //   }

      // If the codec is available, set it as the default in m line.
      //   const codecIndex = findLine(sdpLines, 'a=rtpmap', codec);
      //   console.log('codecIndex', codecIndex);
      //   if (codecIndex) {
      //     // const payload = getCodecPayloadType(sdpLines[codecIndex]);
      //     if (payload) {
      //       sdpLines[mLineIndex] = setDefaultCodec(sdpLines[mLineIndex], payload);
      //     }
      //   }

      sdp = sdpLines.join("\r\n");
      return sdp;
    }
  },
};
</script>

<style></style>
