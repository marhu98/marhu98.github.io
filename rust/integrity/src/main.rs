use glob::glob;
use std::collections::HashSet;
use std::path::Path;
use std::fs;

fn main() {
    let skip = vec!["escalada","scrap"];
    let mut bas_dirs = HashSet::new();
    let dest_dir = vec!["bin","public"];
    let mut all_right = true;
    //for entry in glob("/Users/Paco/Desktop/code/webpage/static/**/*/").expect("Failed to read"){
    for entry in glob("static/**/*/").expect("Failed to read"){
        match entry {
            Ok(path)=>{
                let dir_name = path.into_os_string().into_string().unwrap();
                let mut flag = true;
                for i in &skip {
                    if dir_name.contains(i) {flag=false;}
                }
                //println!("{}",dir_name);
                if flag{
                    bas_dirs.insert(dir_name); 
                }
            },
            Err(e)=>println!("{:?}",e),
        }
    }
    for dest in &dest_dir{
        for path in &bas_dirs {
            let new_path=path.replace("static",dest);
            if !Path::new(&new_path).is_dir() {
                println!("Not existent path detected! {}. \n Creating!",path);
                fs::create_dir_all(&new_path).unwrap();
                all_right=false;
            }
        }
    }
    if all_right {
        println!("No problem in the directory trees detected");
    }
    //println!("{:?}",bas_dirs);
}
