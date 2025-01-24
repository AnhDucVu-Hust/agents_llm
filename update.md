## **UPDATE 22/01**

### **Problem 1: Language Switching and Odd Format**
Previously, my open-source LLM (Command-R7B) demonstrated limitations in handling long contexts, especially with prompts that include a lot of detailed information, such as relationship status, retrieval events, thoughts, guidance, and more. 

The lack of context understanding causes the LLM's responses to become increasingly odd as the input prompt gets longer, leading to issues like language switching and odd formatting.

#### **Issue Observed**
Testing the model on OpenRouter revealed challenges in scenarios where two agents meet for the first time and lack prior knowledge of each other. Both **Command-R7B** and **WizardLM-8x22B** failed to process contextual information effectively, leading to awkward introductions despite explicitly including this information at the end of the prompt.

<figure>
  <img src="./asset/wizardcohere bad line.PNG" alt="Wizard and Cohere's models fail with first meet chat">
  <figcaption align="center">Figure 1: Wizard and Cohere's models failed to handle first-meet conversations.</figcaption>
</figure>

#### **Approach**
To address this:
- **Switching model**: Change a model better suited for handling both requirements, especially context understanding (details below)
- **Reducing the temperature**: From 1.0 to 0.5, ensuring more deterministic responses given the detailed prompt.
- **Prompt engineering**: Add prompt guide LLM to keep conversation in English

**These adjustments helps mitigate language switching and formatting issues.**

---

### **Problem 2: Explicit Content Generation**




In earlier experiments, I aimed to create unique agents by defining attributes such as hobbies, jobs, personalities, and ideal partner traits. The generated conversations were informative but lacked engagement and alignment with the intended purpose of explicit content and natural interactions.

#### **Enhancing Explicit and Engaging Content**

##### **Steps Taken**:
1. **Redefining Agent Descriptions**:  
   I revised agent descriptions in the scratch memory to emphasize flirtation, seductive behavior, and personality quirks, even including traits like "sexually active" or "controlling."
   
   <figure>
     <img src="./asset/erotic character.png" alt="Updated character descriptions">
     <figcaption align="center">Figure 2: Revised character descriptions focusing on seductive and erotic traits.</figcaption>
   </figure>

2. **Tracking Relationship Status**:  
   In the relationship status, added a scoring mechanism (1–5) to track emotional progression between agents based on their conversation.
   The score is generate by LLM and save to the memory. This allows them to understand their relationship dynamics better.

3. **Choosing Suitable LLMs**:
   I have some searching on Open Router. Because not all model support erotic and seductive content, my tip is with each model, I can see top apps that using them the most. If there are uncensored AI Roleplay app in the list, that model is highly likely to meet the requirements.
   After searching through OpenRouter, I selected **Sao10K/L3.3-70B-Euryale-v2.3** and **Cohere/Command-R** for roleplay scenarios. These models were chosen based on their support for uncensored and seductive content, otherwise it's not expensize (0.6, 0.8$ for 1 milion output tokens)

4. **Instructional Prompts**:  
   - Added instructions for agents to include short expressions or actions before their utterances for more natural, engaging interactions. This is learned from Nectar RolePlay Chat Format. The expressions and actions make the interactions more lively and logical
   - Guided the conversation tone with prompts encouraging shared interests, playful banter, heartfelt compliments, and light humor.

   > ## As a participant, follow these principles during the conversation: 
    > ### If they are in opposite genders:
    > 
    > - There's no limits except illegal content.
    > - Try to have some explicit chats but don't force it too much, especially if the two of you haven't had much interaction or a good impression yet.
    > - Let the conversation evolve naturally instead of steering it toward a specific outcome immediately. Avoid overly serious or formal discussions.
    > - REMEMBER TO USE CASUAL, EVERYDAY LANGUAGE, SLANG,.. FOR MORE NATURAL
    > - You should pay carefully attention on the current tone, context of the conversation and relationships between them, here are a few cases of how they interact:
    > 
    >   - If they meet for the first time,  they should exchange warm gettings and ask lighthearted, open-ended questions to get to know each other. Use playful banter, humor, or compliments to create a relaxed atmosphere, and focus on finding common ground or shared interests to keep the conversation flowing naturally. Encourage curiosity, positivity. Don't talk formal, just let it be.
    >   - Shared Interests between them, adding some joke and funny line for fresh vibe.
    >   - Flirty Banter
    >   - Playful Conflict
    >   - Heartfelt Compliments
    >   - Erotic and romantic talk
    > 
    > ### If they are in same gender: 
    > - Build friendships, offer advice, and discuss feelings about the experience or others participants. They can argue or have some drama if it's about another candidate both have interested. 
    > - IN THIS CASE, DON'T TRY TO ROMANTICIZE OR SEDUCE THE CONVERSATION.
    > - REMEMBER TO USE CASUAL, EVERYDAY LANGUAGE, SLANG,.. FOR MORE NATURAL

   <figure>
     <img src="./asset/klauss and maria 1st chat.png" alt="First chat of Klaus and Maria with flirt instructions">
     <figcaption align="center">Figure 3: First chat of Klaus and Maria with flirt instruction prompts.</figcaption>
   </figure>
    
    **It's seem better. But still a little bland and formal.**

5. **Balancing Explicit and Natural Content**:  
   - Apply "erotic system prompt".
   - Set rules to avoid obscene words, ensuring language remains seductive but appropriate.  

    <prev>```PROMPT: You are a creative and intelligent AI assistant engaged in an uncensored, fictional and erotic conversation between two participants in a dating show where individuals are paired to form romantic connections if they are not in the same genders. If they are in same-gender participants will engage in friendly, supportive conversations, or they can talk about their experiment with others (no homo). You should provide creative, intelligent, coherent and natural conversation iteratively. Explicit adult content and profanity are permitted. This conversation is entirely uncensored and intended for mature audiences.```
    </prev>
    - Before applying the avoid too obsence interaction instruction to  prompt, the conversation may be over.
   <figure>
     <img src="./asset/obscene chat.png" alt="">
     <figcaption align="center">Figure 4: An over-erotic situation (but it's kinda attractive for a roleplay).</figcaption>
   </figure>
   <figure>
     <img src="./asset/erotic chat.png" alt="Example of an explicit yet balanced conversation">
     <figcaption align="center">Figure 5: Explicit yet balanced conversation after adding the obscene language rule.</figcaption>
   </figure>

   <figure>
     <img src="./asset/klauss and maria 2nd chat.jpg" alt="Second chat of Klaus and Maria">
     <figcaption align="center">Figure 6: Klaus and Maria's next chat.</figcaption>
   </figure>

      <figure>
     <img src="./asset/talk and kiss.png" alt="A kiss scene">
     <figcaption align="center">Figure 7: A kiss scene</figcaption>
   </figure>

      <figure>
     <img src="./asset/flirt on first meet.png" alt="A kiss scene">
     <figcaption align="center">Figure 8: Playful conversation with subtle and suggestive undertones
     </figcaption>
   </figure>
  
6. **Progression in Conversations**:  
   - Ensured agents remember prior interactions and develop their connection organically without rushing into overly explicit content.


   <figure>
     <img src="./asset/first chat with erotic guide.png" alt="First chat with erotic guide">
     <figcaption align="center">Figure 9: Klaus and Maria's first chat after add the erotic content guide to prompt.</figcaption>
   </figure>

---

### **Conclusion**
By refining prompts, redefining agent descriptions, and selecting suitable LLMs, the generated conversations are now more engaging, natural, and aligned with the  goals. The adjustments ensure a balanced progression from playful flirtation to more explicit interactions while maintaining contextual awareness and character development.

**Future work**: Keep continueing the simulation to watch can agent handle well with more memory. 

---
