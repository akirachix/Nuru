import './login.css'
const login=()=> {

    return(
      <div className="login">
        <div className="form">
            <form className="login-form">
                <div className='form-container'>
                    <div className='email'>
                        <input type="text" required id="emaill" placeholder="name@domain.com"></input>
                    </div>
    
                    <div className="pass">
                        <input type="password" required id="password" placeholder="password"></input>
                    </div>
    
                    <div>
                        <button className="btn-login" type="submit">Login</button>
                    </div>
                </div>

            </form>
        </div>
      </div>
    );
  }
  export default login;
  