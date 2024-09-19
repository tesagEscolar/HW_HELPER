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
