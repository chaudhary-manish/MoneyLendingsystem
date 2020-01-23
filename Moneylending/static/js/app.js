
var validation = {
    isEmailAddress:function(str) {
        var pattern =/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
        return pattern.test(str);  // returns a boolean
    },
    isNotEmpty:function (str) {
        var pattern =/\S+/;
        return pattern.test(str);  // returns a boolean
    },
    isNumber:function(str) {
        var pattern = /^\d+$/;
        return pattern.test(str);  // returns a boolean
    },
    Namevalidation:function(str){
        var pattern =  /^[a-zA-Z ]+$/;
        return pattern.test(str); 
    },
    SSNvalidation:function(str){
        var pattern =  /^[A-Za-z0-9 ]+$/;
        return pattern.test(str); 
    }
};

function validatecontact()
{
    isvalid =true;
    email =document.contact.email.value;
    subject =document.contact.subject.value;
    messages =document.contact.messages.value;

    if(subject.trim() === "")
    {
        document.getElementById("subject").innerHTML = "Subject Required";
        isvalid =false;
    }

    if(messages.trim() === "")
    {
        document.getElementById("messages").innerHTML = "Message Required";
        isvalid =false;
    }

    if(email.trim() === "")
    {
        document.getElementById("email").innerHTML = "Email Required";
        isvalid =false;
    }
    else if (!validation.isEmailAddress(email))
    {
        document.getElementById("email").innerHTML = "Invalid Email";
        isvalid =false;
    }

    if(isvalid)
    {
        return true;
    }
    else{
        return false;
    }

}

function validateinvitation()
{
    isvalid =true;
    invitemail =document.invitegroup.invitemail.value;
    if(invitemail.trim() === "")
    {
        document.getElementById("invitemail").innerHTML = "Email Required";
        isvalid =false;
    }
    else if (!validation.isEmailAddress(invitemail))
    {
        document.getElementById("invitemail").innerHTML = "Invalid Email";
        isvalid =false;
    }

    if(isvalid)
    {
        return true;
    }
    else{
        return false;
    }

}
function validategroup()
{
    var isvalid= true;
    startdate =document.creategroup.startdate.value;
    payments =document.creategroup.payments.value;
    noofperiod =document.creategroup.noofperiod.value;
    GroupName =document.creategroup.GroupName.value;

    if(!validation.isNotEmpty(GroupName))
    {
        document.getElementById("GroupName").innerHTML = "GroupName Required";
        isvalid =false;
    }

    if(!validation.isNotEmpty(payments))
    {
        document.getElementById("payments").innerHTML = "Payments number Required";
        isvalid =false;
    }
    else if (!validation.isNumber(payments))
    {
        document.getElementById("payments").innerHTML = "Invalid Payments";
        isvalid =false;
    }

    if(!validation.isNotEmpty(noofperiod))
    {
        document.getElementById("noofperiod").innerHTML = "No of period Required";
        isvalid =false;
    }
    else if (!validation.isNumber(noofperiod))
    {
        document.getElementById("noofperiod").innerHTML = "Invalid Period";
        isvalid =false;
    }

    if(isvalid)
    {
        return true;
    }
    else{
        return false;
    }

}
function validateform()
{
    let isvalid = true;
    firstname =document.registorform.firstname.value;
    lastname =document.registorform.lastname.value;
    country =document.registorform.country.value;
    postalcode =document.registorform.postalcode.value;
    email =document.registorform.email.value;
    ssnno =document.registorform.ssnno.value;
    mobileno =document.registorform.mobileno.value;
    phoneno =document.registorform.phoneno.value;
    dateofbirth =document.registorform.dateofbirth.value;

    if(!validation.isNotEmpty(postalcode))
    {
        document.getElementById("postalcode").innerHTML = "Postalcode number Required";
        isvalid =false;
    }
    else if (!validation.isNumber(postalcode) || !(postalcode.length == 6))
    {
        document.getElementById("postalcode").innerHTML = "Invalid Postalcode";
        isvalid =false;
    }

   
    if ( (phoneno.trim().length > 0) && (!validation.isNumber(phoneno) || !(mobileno.length == 10)))
    {
        document.getElementById("phoneno").innerHTML = "Invalid Phone number";
        isvalid =false;
    }
    
    if(!validation.isNotEmpty(mobileno))
    {
        document.getElementById("mobileno").innerHTML = "Mobile number Required";
        isvalid =false;
    }
    else if (!validation.isNumber(mobileno) || !(mobileno.length == 10))
    {
        document.getElementById("mobileno").innerHTML = "Invalid Mobile number";
        isvalid =false;
    }

    if(ssnno.trim() === "")
    {
        document.getElementById("ssnno").innerHTML = "SSN Required";
        isvalid =false;
    }
    else if (!validation.SSNvalidation(ssnno) || !(ssnno.length == 10))
    {
        document.getElementById("ssnno").innerHTML = "SSN not contain any special character and length should be 10";
        isvalid =false;
    }

    
    if(email.trim() === "")
    {
        document.getElementById("email").innerHTML = "Email Required";
        isvalid =false;
    }
    else if (!validation.isEmailAddress(email))
    {
        document.getElementById("email").innerHTML = "Invalid Email";
        isvalid =false;
    }

    if(firstname.trim() === "")
    {
        document.getElementById("firstname").innerHTML = "FirstName Required";
        isvalid =false;
    }
    else if (!validation.Namevalidation(firstname))
    {
        document.getElementById("firstname").innerHTML = "FirstName contains only alphabet";
        isvalid =false;
    }

    if(lastname.trim() === "")
    {
        document.getElementById("lastname").innerHTML = "Lastname Required";
        isvalid =false;
    }
    else if (!validation.Namevalidation(lastname))
    {
        document.getElementById("lastname").innerHTML = "Lastname contains only alphabet";
        isvalid =false;
    }

    if(isvalid)
    {
        return true;
    }
    else{
        return false;

    }
    
}


