

//window.web3 = new Web3(web3.currentProvider);

const m_contract_abi = [{"inputs":[{"internalType":"address[]","name":"_airdrops","type":"address[]"},{"internalType":"address","name":"_rewardPool","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_team","type":"address"},{"indexed":false,"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"airdropWalletDiv","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"_team","type":"address"},{"indexed":false,"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"rewardClaimed","type":"event"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"AirDropList","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"AirDropWallets","outputs":[{"internalType":"uint256","name":"_balances","type":"uint256"},{"internalType":"uint256","name":"_pendingReward","type":"uint256"},{"internalType":"bool","name":"_isExist","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"DXB","outputs":[{"internalType":"contract IERC20","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_RewardPool","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"auth","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"distributeWallet","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"getReward","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_regAuth","type":"address"}],"name":"setAuth","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_owner","type":"address"},{"internalType":"address","name":"_AirDropWallet","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"transferFromIAirDrop","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contract IERC20","name":"_DXB","type":"address"}],"name":"updatedDXB","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_AirDropWallet","type":"address"}],"name":"viewAirDropReward","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"stateMutability":"payable","type":"receive"}];
const m_contract_address  = '0x31E337607324bcC5Ac17b33854E6DfeC8ACA421a';

const admin_address 		=	'0x1204bdac6e2c38cd08cbf9f7c1bdda5c69e82073';

const check_address = '0xfcF6966547ea0EF986A44be7732D8B884e70158D'

var current_level 		=	1;

var accounts1 				=	[];

//let messageHash 			=	web3.utils.asciiToHex('0');

//let __r 					=	web3.utils.asciiToHex('1');
 
//let __s 					=	web3.utils.asciiToHex('2');

let __v 					=	'';

var m_contract 				=	'';

let reff_id					=	'';

let user_ref_id				=	'';

let buyLevel				=	'';

let buyType					=	'';

let levelPrice				=	'';

let adminFee				=	'';

let signature               =    '';


var currentpage = window.location.pathname;

$(document).on('click','.click_metamaskcls',function(){

if (typeof web3 !== "undefined") {

	window.web3 = new Web3(web3.currentProvider);

	var McontractInfo 	= 	(m_contract_abi);

	m_contract 		= 	new web3.eth.Contract(McontractInfo,m_contract_address);

	

	(async function(){
		
		const accounts = await ethereum.request({
	            method: 'eth_accounts'
	        })
	        .then()
	        .catch((accounts) => {
	            if (error.code === 4001) {
	                console.log('Please connect to MetaMask.')
	            } else {
	            	console.log(error)
	            }
	        });	
	        if (accounts.length == 0) {
	        	msg ='Your metamask account is locked please unlock';
				type ='error';
				enableAccount()
				validate_msg(type,msg)
	        }
	        else{

	        	accounts1 = accounts;
	        	message = accounts1[0]+"celan"+Date.now();
	        	var address = accounts1[0];
				var values= {'address':address }
				$.ajax({
				url: '/global/connectmetamask/',
				csrfmiddlewaretoken: "{{ csrf_token }}",
				headers: {
	  			'Accept': 'application/json',
	  			'Content-Type': 'application/json'
	     		},
		        type: 'post',
		        data:JSON.stringify(values),
		        success: function(content){ 
	            var json_obj = JSON.parse(content.content);           
	            if (json_obj.status == 'successlogin'){
	              type ='success';
	              msg ='Metamask connected successfully.';
	              window.location.href = '/global/walletdetails/';
	              validate_msg(type,msg)
	            }
	            else if (json_obj.status == 'successregistered'){
	              type ='success';
	              msg ='Metamask connected successfully.';
	              window.location.href = '/global/walletdetails/';
	              validate_msg(type,msg)
	            }else{
	              type ='error';
	              msg ='Metamask not connected';
	              validate_msg(type,msg)
	            }
		        },
		        });
	        }
	        
	}) ();
}
else{
	
	msg ='Metamask addon not installed in browser.';
	type ='error';
	validate_msg(type,msg)
}

function validate_msg(type,message){
			      if (type =='success'){
			        var success_text =  message;
			        Lobibox.notify('success', {
			        title:'Success',
			        continueDelayOnInactiveTab: false,
			        pauseDelayOnHover: true,
			        sound: false,
			        position: 'right top',
			        msg: success_text
			        });

			      }
			      if (type =='error'){
			        var error_text = message
			        Lobibox.notify('error', {
			        title:'Error',
			        continueDelayOnInactiveTab: false,
			        pauseDelayOnHover: true,
			        sound: false,
			        position: 'right top',
			        msg: error_text
			        });
			      }
}	

});
if (typeof web3 !== "undefined") {
	window.web3 = new Web3(web3.currentProvider);

	var McontractInfo 	= 	(m_contract_abi);

	m_contract 		= 	new web3.eth.Contract(McontractInfo,m_contract_address);

	
	(async function(){
			var currentpage = window.location.pathname;
			console.log(currentpage)
			if (currentpage == '/global/walletdetails/'){

					const accounts = await ethereum.request({
			            method: 'eth_accounts'
			        })
			        .then()
			        .catch((accounts) => {
			            if (error.code === 4001) {
			                console.log('test1')
			            } else {
			            	console.log('test2')
			            }
			        });
			        console.log("accounts",accounts);
			        if (accounts.length == 0) {
			        	msg ='Your metamask account is locked please unlock.';
						type ='error';
						validate_msg(type,msg)
			        }
			        else{
			        	accounts1 = accounts;
		        		message = accounts1[0]+"celan"+Date.now();
		        		var address = accounts1[0];
		        		$('.walletaddressheader').html(address);
						$('#walletaddress').html(address);
						
						m_contract.methods.AirDropWallets(address).call().then(function(walletinvest){
						let walletinvestresult = walletinvest;
						let walletbalance =walletinvest[0];
						let walletpendingreward = walletinvest[1];
						let walletstatus = walletinvest[2];
						
						$('#walletbalance').html(walletbalance);
						console.log(walletstatus,'walletstatus')
						
						if (walletstatus == true){
							$(".claimshow").hide();
							$(".claimhide").show();
						}else if (walletstatus == false){
							$(".claimhide").hide();
							$(".claimshow").show();
						}
						});
						/*m_contract.methods.viewInvestorReward(address).call().then(function(Investerreward){
						
						});*/

						$('body').on('click', '#click_claim', function(){
							
							m_contract.methods.getReward().send({from:address}).then(async function(reward){
								console.log('result' ,reward);

							});	
						});
					}
					function validate_msg(type,message){
				      if (type =='success'){
				        var success_text =  message;
				        Lobibox.notify('success', {
				        title:'Success',
				        continueDelayOnInactiveTab: false,
				        pauseDelayOnHover: true,
				        sound: false,
				        position: 'right top',
				        msg: success_text
				        });
				      }
				      if (type =='error'){
				        var error_text = message
				        Lobibox.notify('error', {
				        title:'Error',
				        continueDelayOnInactiveTab: false,
				        pauseDelayOnHover: true,
				        sound: false,
				        position: 'right top',
				        msg: error_text
				        });
				      }
		    		}
		      	}
		}) ();
}
      	
async function enableAccount() {

	const accounts 	= 	await ethereum.enable();

	accounts1 		= 	accounts;

	setTimeout(function(){ 
	  document.getElementById("click_metamask").click();
	}, 3000);
 
}