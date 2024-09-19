Here’s a prettified version of your Markdown file with proper placement and styles for the images:

---

# Get Started

1. Visit the [Google Script environment](https://script.google.com/u/1/home/)
2. On the top right, click the **Create New Project** button.

   ![image](https://github.com/user-attachments/assets/6a9292c1-1991-46e0-b0fa-7ab589736bd7)

3. On the left-hand side menu, you'll see the **Libraries** option.  
   **Click on the + icon.**

   ![image](https://github.com/user-attachments/assets/49e6cc59-1645-42dd-931d-b41ddd16c603)

4. The following pop-up will appear:

   ![image](https://github.com/user-attachments/assets/273b5294-35ba-4678-802f-36a02a9d99c9)

---

## Add the Library to Your Script Project

### Use the following key to search for the library:

- **Key**: `1VK1pahv2k9SaBAcV0yBM7iyA6fdkkVpZDj_yJtpNHNLxmMD7jyrwY1We`

### Paste it in the **ID Field** and click **Search**:

   ![image](https://github.com/user-attachments/assets/a416cb69-7ae4-4f11-9234-42d933dfd19a)

5. In the **Version** field, you will see a couple of options:
   - **HEAD (development mode)**: This provides the latest version but could be unstable as it's a development version.
   - **8 (latest number version)**: Select the highest number for the latest stable version.

6. The **Identifier Field** controls how you want the library to be invoked in your code. You can leave it as is for the same results as in this guide.

7. **Click on Add** to continue.

---

## Implementation of the Library

Add the following code to your script:

   ![image](https://github.com/user-attachments/assets/04e64716-a9e3-4492-afec-13ce2df26cf6)

---

### Test the Library

Temporarily comment out the `hwHelper.run()` function and click the **Execute** button at the top to test whether the library was loaded properly.

   ![image](https://github.com/user-attachments/assets/ba2d5e9b-5653-4c4a-bf3f-8fec918dc444)

You should see the following prompt:

   ![image](https://github.com/user-attachments/assets/268495c0-2e7b-47d4-bd31-394f572ac07d)

Uncomment `hwHelper.run()` to prepare it for execution.

---

### Field Explanations:

Set the parameters to suit your needs:
- **HW_TITLE**: The title (copied) of a specific homework assignment you want the assistant to solve. Use `'ALL'` to check all pending assignments.
- **NAME**: Your student name. This will be used to fill your essays, works, slides, etc.
- **REG**: Your student registration. This will also be used to fill your works.
- **CLASSES**: An array of exact class names where the bot will search for assignments.
- **TASK_LIST_NAME**: The name of the task list where notifications about completed assignments will be posted.  
  *Note: This feature is still under development.*

---
Here’s the enhanced version of your Markdown file with proper placement and formatting for the images:

---

# Set the API Keys

In this project, we are using two main services that require API keys. Here’s how to set them up.

1. **Click** on the left menu and select the gear icon labeled **Project Configuration**.

   ![image](https://github.com/user-attachments/assets/cccc3a0a-d390-470e-96ef-a37da89bc6a7)

2. Scroll to the bottom of the page and **click** the button labeled **Add Command Sequence Property**.

   ![image](https://github.com/user-attachments/assets/9f9e3f8a-a9a8-4dc8-b538-4a210fd8cb9a)

This will open two fields: **Property** and **Value**. In the **Property** field, enter the alias for your API key as it will appear in your code. Let’s see the two API keys that we will place here:

---

## Gemini API Key

1. In the **Property** field, use the name `GEMINI_API_KEY` (you can use any name, but ensure it matches your code).

   ![image](https://github.com/user-attachments/assets/1c77068f-cb9d-45f3-9492-4d77168c88c0)

2. To get the Gemini API key, visit [Google's AI Studio](https://aistudio.google.com/app/u/1/apikey) and log in with the preferred account.

3. On the left-side menu, **Click** on **Get API Key**.

   ![image](https://github.com/user-attachments/assets/bc7e354b-daf5-47c4-a3a2-5443928cf49e)

4. Then select the **Create API Key** button.

   ![image](https://github.com/user-attachments/assets/922473dc-c2aa-445d-9336-64db9c7df81c)

5. A pop-up will display your new API key. **Copy** the key and paste it into the **Value** field in the Google Script input.

   ![image](https://github.com/user-attachments/assets/6f0b9039-360a-4452-a13d-f044131f75d8)

6. **Click** the **Save Command Sequence Property** button just below the input.

---

## GitHub API Key

Add another **Command Sequence Property** for the GitHub API key.

1. To retrieve or generate your **GitHub API Key** (Personal Access Token), follow these steps:

   - Go to [GitHub.com](https://github.com) or go directly to the [GitHub API Key Settings](https://github.com/settings/tokens) and log in to your account.
   - Click on your profile picture in the top-right corner and select **Settings**.

2. **Access Developer Settings**:

   - In the left-hand sidebar, scroll down and click **Developer settings**.
   - Click on **Personal Access Tokens**.
   - Then click **Tokens (classic)** to view or generate classic tokens.
   - Alternatively, use **Fine-grained tokens** for more specific permissions (recommended for newer projects).

3. **Generate a New Token**:

   - Click **Generate new token**.
   - Select the necessary **scopes**. For this project, ensure *repo status* and *public_repo* are selected.

   ![image](https://github.com/user-attachments/assets/54be8443-7a23-4713-9455-bf0975b37ee9)

4. **Save your token** immediately after generation, as it will not be displayed again.

   ![image](https://github.com/user-attachments/assets/7acb13f3-bdd0-4edf-8169-442f4ab7da66)

5. Copy and paste the generated GitHub API key into the **Google Script** Property Value field.

   ![image](https://github.com/user-attachments/assets/4d06f41b-ad9b-47fe-b0d3-96463361feec)

6. Finally, **click** the **Save Properties** button.

---

## Set API Keys in the Library

Now, we need to pass these keys to the library so that it can use them. Back in the script editor, add the following lines of code:

```javascript
const GITHUB_USERNAME = 'ThaManWithoutFear';
const GITHUB_REPO_NAME = 'HW_HELPER';

const properties = PropertiesService.getScriptProperties().getProperties();
const GEMINI_API_KEY = properties['GEMINI_API_KEY'];
const GITHUB_API_KEY = properties['GITHUB_API_KEY'];

const GH_CREDENTIALS = {
  githubToken: GITHUB_API_KEY,
  username: GITHUB_USERNAME,
  repoName: GITHUB_REPO_NAME
};
```

Here, you define your GitHub username and the repo name you want to use. You can leave this option blank, and it will default to the `'HW_HELPER'` repo name.

   ![image](https://github.com/user-attachments/assets/0253825c-2292-437e-ada0-e83afbfc4cd1)

Then, add the parameters to the `run` function:

```javascript
hwHelper.run(HW_TITLE, NAME, REG, GH_CREDENTIALS, GEMINI_API_KEY, CLASSES, TASK_LIST_NAME);
```
   ![image](https://github.com/user-attachments/assets/0cbaaa5b-bbe1-4849-8db9-a821f4843f4a)


---
## Set the Triggers

On the left-side menu, click on the **Clock Icon**:

   ![image](https://github.com/user-attachments/assets/a9c326ce-0bd7-45aa-a3fc-31eec693739a)

You'll be taken to the following page:

   ![image](https://github.com/user-attachments/assets/53feb314-569f-438b-9878-90cb281a47e6)

1. Click on the **Add Trigger** button in the bottom-left corner of the page. The following pop-up will appear:

   ![image](https://github.com/user-attachments/assets/b6b9c93e-5f1c-45ae-a568-895095385d88)

#### Input the following options:

- **Function to execute**: `main`
- **Deploy to execute**: `Main (Principal)`
- **Source of the event**: `Time-based (Según tiempo)`
- **Time-based Trigger**: `Timer by days (Temporizador por días)`
- **Hour**: 22:00 to 23:00

   ![image](https://github.com/user-attachments/assets/8e97f216-071c-41ec-80fb-a1037ade50f4)
   ![image](https://github.com/user-attachments/assets/715cb55a-9089-49b7-92b2-3140f1d2d3be)

2. **Click on the Save button to continue.**

---

### Your new trigger should appear as follows:

   ![image](https://github.com/user-attachments/assets/edf2118d-38fd-42a5-b13f-cac5b2485def)

---

## That's it! 🎉🎉🎉 The assistant will run between 10 PM and 11 PM and do your homework.

--- 

This version structures your instructions cleanly and ensures that the images are placed correctly while maintaining readability.
