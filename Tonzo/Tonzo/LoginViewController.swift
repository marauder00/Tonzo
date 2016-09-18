//
//  ViewController.swift
//  Tonzo
//
//  Created by Mara Gagiu on 2016-09-18.
//  Copyright © 2016 Mara Gagiu. All rights reserved.
//

import UIKit

class LoginViewController: UIViewController {
    
    //UI Component Declarations
    @IBOutlet weak var userDisplay: UITextField!
    @IBOutlet weak var passwordDisplay: UITextField!
    
    //Data Component Declarations
    private var username:String?
    private var password:String?

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    @IBAction func logIntoApp(_ sender: UIButton) {
        //first process text in textfields into appropriate parameters
        username = userDisplay.text
        password = passwordDisplay.text
        
        //now to check if the users are actually a part of the system..
        
        
    }

}

