async function getGithubUsers(userNames)
{
    console.log('1. Starting to fetch user data...');
    let jobs = []; // array of Promises
    for (let name of userNames) {
        let response = fetch(`https://api.github.com/users/${name}`).then(
            successResponse => {
                if (successResponse.status != 200) {
                    return null;
                } else {
                    return successResponse.json();
                }
            },
            failResponse => {
                return null;
            }
        );
        jobs.push(response);
    }
    let results = await Promise.all(jobs);
    console.log('4. Finished fetching user data...');
    return results;
}

function processOtherStuff() {
    console.log('2. Processing other stuff...');
}

function moreProcessing() {
    console.log('3. Doing more work...');
}

// Main execution
console.log('--- Starting program ---');
getGithubUsers(
        ["khoaguin", "shubham3121", "rasswanth-s", "iamtrask", "madhavajay", "yashgorana"]
    ).then(
        users => {
            // print users name and location
            for (let user of users) {
                if (user) {
                    console.log(`User: ${user.login}, Location: ${user.location}`);
                } else {
                    console.log('User not found');
                }
            }
        },
        error => {
            console.log('Error:', error);
        }
    )
// );  // This is async, so it doesn't block
processOtherStuff();  // This runs immediately
moreProcessing();     // This runs immediately too