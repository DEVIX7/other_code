--[[ 01/05/2024 ; devix7 ]]
local args = {
    [1] = "Troops",
    [2] = "Option",
    [3] = "Set",
    [4] = {
        ["Troop"] = workspace:WaitForChild("Towers"):WaitForChild("1"),
        ["Name"] = "Bomb 1", --[[ Bomb 1 , Bomb 2 ]]
        ["Value"] = "Ice" --[[ Fire , Ice , Poison , Confusion ]]
    },
}

game:GetService("ReplicatedStorage"):WaitForChild("RemoteFunction"):InvokeServer(unpack(args))

