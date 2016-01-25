<?php
$field_name = $_POST['cf_name'];
$field_email = $_POST['cf_email'];
$field_message = $_POST['cf_message'];

$mail_to = 'ogjdne@gmail.com'; //put commas between additional emails

$subject = 'A visitor wants to contact you' . $field_name;

$body_message = 'From: '.$field_name."\n";
$body_message .= 'E-mail: '.$field_email."\n";
$body_message .= 'Message: '.$field_message;

$headers = "From: $cf_email\r\n";
$headers .= "Reply-To: $cf_email\r\n";

$mail_status = mail($mail_to, $subject, $body_message, $headers);

if ($mail_status) { ?>
	<script language="javascript" type="text/javascript">
		//Print message
		alert('Thank you for messaging me, I hope to get back to you soon!");
		//Redirect to page
		window.location = 'contactPHP.html';
	</script>
<?php
}	
else { ?>
	`<script language="javascript" type="text/javascript">
		//Print message
		alert('Message was not sent. Please email ogjdne@gmail.com');
		//Redirect page
		window.locaction ='contact_page.html';
	</script>
<?php
}?>