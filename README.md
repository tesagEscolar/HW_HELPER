## Get Started
* Visit the [Google Script environment](https://script.google.com/u/1/home/)
* On top right click the *create new project* button
![image](https://github.com/user-attachments/assets/6a9292c1-1991-46e0-b0fa-7ab589736bd7)

* Create a new Google Script project 
* On the left hand side menu you'll see the option libraries. *CLICK ON THE + ICON*
* The following pop up will prompt:
![image](https://github.com/user-attachments/assets/273b5294-35ba-4678-802f-36a02a9d99c9)


## Add the library to your script project
### Use the following key to search for library
*key*:1VK1pahv2k9SaBAcV0yBM7iyA6fdkkVpZDj_yJtpNHNLxmMD7jyrwY1We

### Paste it in the ID Field and click on *search*:
![image](https://github.com/user-attachments/assets/a416cb69-7ae4-4f11-9234-42d933dfd19a)

Click on the version field and you will see a couple of options:
* HEAD (development mode): This will give you the version of the library with the latest changes, although it could malfunction as it is a development version.
* 8 (latest number version): Click on the highest number to get the latest functioning version of the library.

The identifier field control how tou want the library to be invoked inside your code. You can leave it as is, to have the same results as in this guide.

*CLICK ON ADD TO CONTINUE*



## Implementation of the library 
Add the following code to your script.
![image](https://github.com/user-attachments/assets/04e64716-a9e3-4492-afec-13ce2df26cf6)

### Test the library
Temporarly Comment the *hwHelper.run()* function and *CLICK* on the execute button at the top to test the library was loaded properly. 
![image](https://github.com/user-attachments/assets/ba2d5e9b-5653-4c4a-bf3f-8fec918dc444)

You should get the following prompt
![image](https://github.com/user-attachments/assets/268495c0-2e7b-47d4-bd31-394f572ac07d)

Uncomment the *hwHelper.run()* to leave it ready to run.

### Field explanations:
Set the parameters to suit your needs:
* HW_TITLE: The title (copyed) of a specific homework you want the assistant to solve. Use 'ALL' to check all pending asigments.
* NAME: Your student name, this is the name that will be used to fill your essays, works, slides etc..
* REG: Your student register, this will be used to fill your essays, works, slides etc...
* CLASSES: An array containing the exact names of the classes from where the bot will look for asigments.
* TASK_LIST_NAME: The name of the task list where notifications of the done asigments will be posted. *NOTE: this feature is still under development*

## Set the triggers
On the left side menu, *CLICK* on the clock icon:
![image](https://github.com/user-attachments/assets/a9c326ce-0bd7-45aa-a3fc-31eec693739a)

You'll be prompted to the next page:
![image](https://github.com/user-attachments/assets/53feb314-569f-438b-9878-90cb281a47e6)

*CLICK* on the button *ADD TRIGGER* on the left inferior corner, of the page. The following popup will apear:
![image](https://github.com/user-attachments/assets/b6b9c93e-5f1c-45ae-a568-895095385d88)

#### Input the following options:
* Function to execute: main
* Deploy to execute: Main (Principal)
* Source of the event: Time based (Según tiempo)
* Time based Trigger: Timer by days (Temporizador por dias)
* Hour: 22:00 to 23:00

![image](https://github.com/user-attachments/assets/8e97f216-071c-41ec-80fb-a1037ade50f4)
![image](https://github.com/user-attachments/assets/715cb55a-9089-49b7-92b2-3140f1d2d3be)

*CLICK on the Save button to continue*

### You are all set your new trigger should appear:
![image](https://github.com/user-attachments/assets/edf2118d-38fd-42a5-b13f-cac5b2485def)

## Thats it!! 🎉🎉🎉 the assistant will run some time between 10pm - 11pm and do your homework.  

