/*
** F1 bet for sohu sports
** author dongli
** date 2013.04.03
*/
(function($){
	var user_main = $('.user-main'),
		user = $('.user'),
		rate_right = $('.rate-right'),
		rate_left = $('.rate-left'),
		rate_middle = $('.rate-middle'),
		submit = $('.submit'),
		submit_all = $('.submit-all');

	var controller = {
		login : function(){
			var info = $('.user-option span');
			info.html('');
			if($('.eml').val() != '' && $('.pwd').val() != ''){
				$.ajax({
					type : 'POST',
					url : '/f1/login/',
					data : {
						'userid' : $('.eml').val(),
						'password' : $('.pwd').val()
					},
					success : function(e){
						if(typeof(JSON) == 'undefined'){
							data = eval("("+ e +")");
						}
						else{
							data = JSON.parse(e);
						}
						if(data.code == 1){
							userid = data.userid;
							score = data.score;
							var html = '<div class="user-info"><img src="/f1/static/images/avatar.png"><div class="user-name">欢迎您，<br/>'+ data.userid +'</div></div><div class="guess-info"><p>总积分：<span>'+ parseFloat(data.score).toFixed(1) +'</span>分</p><p>排&nbsp;&nbsp;&nbsp;名：<span>'+ data.index +'</span>名</p>';
							if(!data.sign)
								html += '<a class="sign">签到</a>';
							else
								html += '<a class="signed">已签到</a>';
							html +=	'</div><a class="history" href="/f1/history">个人历史记录</a><div><a href="#" class="logout">退出</a><a href="#" class="change">修改个人信息</a><a href="https://passport.sohu.com/web/updateInfo.action?modifyType=password" target="_blank" class="forgetpwd">修改密码</a></div><div class="pop"><p>姓名：<input type="text" class="name"></p><p>手机：<input type="text" class="phone"></p><p>地址：<input type="text" class="address"></p><p>邮编：<input type="text" class="code"></p><p><input type="submit" value="确定" class="pop-save"><input type="submit" value="取消" class="pop-cancel"></p></div>';
							user_main.html(html);
						}
						else{
							if(data.errortype == 3)
								info.html('用户名密码错');
							else
								info.html('网络错误，请重试');
						}
					},
					error : function(e){
						console.log(e);
						info.html('网络错误，请重试');
					}
				})
			}
			else{
				info.html('用户名或密码不能为空');
			}
		},
		logout : function(){
			$.ajax({
				url : '/f1/logout/',
				type : 'POST',
				success : function(){
					var html = '<p>电子邮件</p><input type="text" class="eml" name="userid"><p>密码</p><input type="password" class="pwd" name="password"><div class="user-option"><span></span><a href="http://passport.sohu.com/web/recover.jsp" target="_blank">忘记密码?</a></div><div class="user-btn"><a href="javascript:;" class="login">登录<i></i></a><a href="https://passport.sohu.com/web/dispatchAction.action?ru=http://f1.sohu.com/s2013/game/" target="_parent" class="register">立即注册</a></div>';
					user_main.html(html);
					userid = null;
				}
			})
		},
		enterPwd : function(e){
			if(e.keyCode == 13)
				$('.login').trigger('click');
		},
		sign : function(){
			$.ajax({
				url : '/f1/sign/',
				type : 'POST',
				data : {'userid':userid},
				success : function(e){
					if(typeof(JSON) == 'undefined'){
							data = eval("("+ e +")");
						}
						else{
							data = JSON.parse(e);
						}
					if(data.code == 1){
						$('.sign').html('已签到').addClass("signed").removeClass("sign");
						$('.guess-info span:eq(0)').html(parseFloat(data.score).toFixed(1));
					}
				},
				error : function(){

				}
			});
		},
		addRate : function(self){
			var rate_text = self.parent().find('input');
			rate_text.val(parseInt(rate_text.val())+1);
			return false;
		},
		minusRate : function(self){
			var rate_text = self.parent().find('input');
			if(parseInt(rate_text.val()) > 0)
				rate_text.val(parseInt(rate_text.val())-1);
			return false;
		},
		testNum : function(self){
			var reg = /^[0-9]+$/g;
			if(!reg.test(self.val()))
				self.val(0);
		},
		submitRate : function(self, flag){
			var rate_score = parseInt(self.parent().parent().find('input').val());
			if(userid){
				if(rate_score > score){
					alert("竞猜分不能大于最大积分！");
					return false;
				}
				else if(rate_score <= 0){
					if(flag)
						alert("请输入竞猜分！");
					return false;
				}
				else{
					$.ajax({
						url : '/f1/submit/',
						type : 'POST',
						data : {'userid':userid,'races':races,'score':rate_score,'driver':self.attr("driver")},
						success : function(e){
							if(typeof(JSON) == 'undefined'){
							data = eval("("+ e +")");
						}
						else{
							data = JSON.parse(e);
						}
							if(data.code == 1){
								score -= rate_score;
								$('.submit-info').html("竞猜成功");
								$('.guess-info span:eq(0)').html(data.score);
							}
							else{
								alert("竞猜分不能大于最大积分！");
							}
						},
						error : function(){
							$('.submit-info').html("竞猜失败，请重试！");
						}
					});
				}
			}
			else{
				alert("请先登录");
				return false;
			}	
		},
		submitAllRate : function(){
			var temp = 0;
			for(var i = 0;i < 22;i++){
				temp += parseInt($('.rate-middle:eq('+i+')').val());
			}
			if(temp == 0){
				alert("请输入竞猜分！");
				return false;
			}
			else if(temp <= score){
				for(var i = 0;i < 22;i++){
					(function(i){
						setTimeout(function(){
							controller.submitRate($('.submit:eq('+i+')'),0);
						},100*i);
					})(i)
				}
				return false;
			}
			else{
				alert("下注分不能大于最大积分！");
				return false;
			}
		},
		changeInfo : function(){
			$.ajax({
				url : '/f1/change/',
				type : 'POST',
				success : function(e){
					if(typeof(JSON) == 'undefined'){
						data = eval("("+ e +")");
					}
					else{
						data = JSON.parse(e);
					}
					$('.name').val(data.name);
					$('.phone').val(data.phone);
					$('.address').val(data.address);
					$('.code').val(data.code);
					$('.pop').fadeIn();
				},
				error : function(){
					alert("网络错误，请重试！");
				}
			});
		},
		changeCancel : function(){
			$('.pop').fadeOut();
		},
		changeSave : function(){
			$.ajax({
				url : '/f1/changeSave/',
				type : 'POST',
				data : {"name":$('.name').val(),"phone":$('.phone').val(),"address":$('.address').val(),"code":$('.code').val()},
				success : function(){
					$('.pop').fadeOut();
				},
				error : function(){
					alert("输入错误，请重试！");
				}
			})
		}
	};

	var bindEvent = function(){
		user.delegate('.login','click',function(){
			controller.login();
		});
		user.delegate('.logout','click',function(){
			controller.logout();
		});
		user.delegate('.pwd','keydown',function(){
			controller.enterPwd(event);
		});
		user.delegate('.sign','click',function(){
			controller.sign();
		});
		user.delegate('.change','click',function(){
			controller.changeInfo();
		});
		user.delegate('.pop-save','click',function(){
			controller.changeSave();
		});
		user.delegate('.pop-cancel','click',function(){
			controller.changeCancel();
		});
		rate_right.bind('click',function(){
			controller.addRate($(this));
		});
		rate_left.bind('click',function(){
			controller.minusRate($(this));
		});
		rate_middle.bind('keyup',function(){
			controller.testNum($(this));
		});
		submit.bind('click',function(){
			controller.submitRate($(this),1);
		});
		submit_all.bind('click',function(){
			controller.submitAllRate();
		});
	};

	bindEvent();
})(jQuery)
