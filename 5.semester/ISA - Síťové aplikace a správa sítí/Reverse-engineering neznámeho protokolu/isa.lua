-- VUT FIT ISA 2021 Project - Reverse engineering of unknown protocol
-- Author: Vanessa Jóriová
-- Lua dissector for custom ISA protocol


isamail_protocol = Proto("ISA",  "ISA Protocol")

isamail_protocol.fields = {}

function isamail_protocol.dissector(buffer, pinfo, tree)
  length = buffer:len()
  if length < 3 then return end
  if buffer(length - 1, 1):string() ~= ")" then
    pktinfo.desegment_len = DESEGMENT_ONE_MORE_SEGMENT
    pktinfo.desegment_offset = 0
    return
  end

  pinfo.cols.protocol = isamail_protocol.name
  local len = buffer:len()


  local subtree = tree:add(isamail_protocol, buffer(), "ISA Protocol Data")
  -- length and raw data
  subtree:add("Data length: ", len)
  subtree:add(buffer(0,len),"Raw data: " .. buffer(0,len):string())

  --check if server or client
  local sender = "default"
  local status = "default"   
  local second_third_byte = buffer(1,2):string()

  if second_third_byte == "ok" then
    sender = "server"
    status = "ok"
  elseif second_third_byte == "er" then
    sender = "server"
    status = "err"
  else
    sender = "client"
  end

  subtree:add("Sender: ", sender)
  if sender == "server" then
    if status == "ok" then
        subtree:add(buffer(1,2), "Status: ", status)
    elseif status == "err" then    
        subtree:add(buffer(1,3), "Status: ", status)
    end
    subtree:add("Type: ", "response")
  elseif sender == "client" then
    subtree:add("Type: ", "request") 
  end
  

  local current_index = 0
  --getting client action
  if sender == "client" then
    --skipping first (
    current_index = incrementIndex(current_index, 1, buffer)
    if current_index < 0 then return 0 end
    local action = ""
    local loaded_bytes = 0
    local current_byte = buffer(1,1)
    while true do


        current_byte = buffer(current_index,1)
        if current_byte:string() == " " then
            break
        end
        action = action .. current_byte:string()
        loaded_bytes = loaded_bytes + 1
        current_index = incrementIndex(current_index, 1, buffer)
        if current_index < 0 then return 0 end
    end
    subtree:add(buffer(1,0+loaded_bytes), "Action: ", action)
    current_index = incrementIndex(current_index, 1, buffer) -- skipping white space 
    if current_index < 0 then return 0 end 
    
    
    --- SUBTREES FOR CLIENT ACTIONS ---

    -- REGISTER AND LOGIN    
    if action == "register" or action == "login" then
        --len-bytes_from_bigging-1 -> skipping last )
        local register_subtree = subtree:add(buffer(current_index, len-current_index-1), "Request details ")

        -- user
        current_index = incrementIndex(current_index, 1, buffer) --skipping first "  
        if current_index < 0 then return 0 end
        local user= ""
        local loaded_bytes = 0
        
        user, loaded_bytes = stringUntilQMarks(current_index, buffer)
        if loaded_bytes < 0 then return 0 end

        current_index = incrementIndex(current_index, loaded_bytes, buffer)
        if current_index < 0 then return 0 end

        register_subtree:add(buffer(current_index-loaded_bytes, loaded_bytes), "User: ", user)

        -- password
        local password= ""
        current_index = incrementIndex(current_index, 3, buffer) --skipping " "
        if current_index < 0 then return 0 end

        password, loaded_bytes = stringUntilQMarks(current_index, buffer)
        if loaded_bytes < 0 then return 0 end
        
        current_index = incrementIndex(current_index, loaded_bytes, buffer)
        if current_index < 0 then return 0 end
        register_subtree:add(buffer(current_index-loaded_bytes, loaded_bytes), "Encoded password: ", password)

        pinfo.cols.info = action .. " request: "  .. user


    -- LOGOUT, LIST
    elseif action == "logout" or action == "list" then
        local logout_subtree = subtree:add(buffer(current_index, len-current_index-1), "Request details ")
        -- user
        current_index = incrementIndex(current_index, 1, buffer) --skipping first "  
        if current_index < 0 then return 0 end
        local found_string = ""
        local loaded_bytes = 0
        
        found_string, loaded_bytes = stringUntilQMarks(current_index, buffer)
        if loaded_bytes < 0 then return 0 end

        ccurrent_index = incrementIndex(current_index, loaded_bytes, buffer)
        if current_index < 0 then return 0 end
        logout_subtree:add(buffer(current_index-loaded_bytes, loaded_bytes), "Session token: ", found_string)    
         
        pinfo.cols.info = action .. " request "

    -- SEND 

    elseif action == "send" then
        local send_subtree = subtree:add(buffer(current_index, len-current_index-1), "Request details ")
        -- sender
        
        current_index = incrementIndex(current_index, 1, buffer) --skipping first "  
        if current_index < 0 then return 0 end
        
        local sender = ""
        local loaded_bytes = 0
        
        sender, loaded_bytes = stringUntilQMarks(current_index, buffer)
        if loaded_bytes < 0 then return 0 end


        current_index = incrementIndex(current_index, loaded_bytes, buffer)
        if current_index < 0 then return 0 end


        send_subtree:add(buffer(current_index-loaded_bytes, loaded_bytes), "Session token: ", sender)
        
        -- recipient
        
        current_index = incrementIndex(current_index, 3, buffer) --skipping " "
        if current_index < 0 then return 0 end

        local recipient = ""
        
        recipient, loaded_bytes = stringUntilQMarks(current_index, buffer)
        if loaded_bytes < 0 then return 0 end

        current_index = incrementIndex(current_index, loaded_bytes, buffer)
        if current_index < 0 then return 0 end

        send_subtree:add(buffer(current_index-loaded_bytes, loaded_bytes), "Recipient: ", recipient)

        -- subject
        current_index = incrementIndex(current_index, 3, buffer) --skipping " "
        if current_index < 0 then return 0 end

        local subject = ""
        
        subject, loaded_bytes = stringUntilQMarks(current_index, buffer)
        if loaded_bytes < 0 then return 0 end

        current_index = incrementIndex(current_index, loaded_bytes, buffer)
        if current_index < 0 then return 0 end

        send_subtree:add(buffer(current_index-loaded_bytes, loaded_bytes), "Subject: ", subject)

        -- messege
        current_index = incrementIndex(current_index, 3, buffer) --skipping " "
        if current_index < 0 then return 0 end

        local messege = ""
        
        messege, loaded_bytes = stringUntilQMarks(current_index, buffer)
        if loaded_bytes < 0 then return 0 end

        current_index = incrementIndex(current_index, loaded_bytes, buffer)
        if current_index < 0 then return 0 end

        send_subtree:add(buffer(current_index-loaded_bytes, loaded_bytes), "Messege: ", messege)

        pinfo.cols.info = action .. " request: " .. recipient .. " " .. subject .. " \"" .. messege .. "\""

-- FETCH
    elseif action == "fetch" then
        local fetch_subtree = subtree:add(buffer(current_index, len-current_index-1), "Request details ")
        -- user
        
        current_index = incrementIndex(current_index, 1, buffer) --skipping first "  
        if current_index < 0 then return 0 end

        local found_string = ""
        local loaded_bytes = 0
        
        found_string, loaded_bytes = stringUntilQMarks(current_index, buffer)
        if loaded_bytes < 0 then return 0 end

        current_index = incrementIndex(current_index, loaded_bytes, buffer)
        if current_index < 0 then return 0 end

        fetch_subtree:add(buffer(current_index-loaded_bytes, loaded_bytes), "Session token: ", found_string)  
        
        current_index = incrementIndex(current_index, 2, buffer) -- skipping " and blank space
        if current_index < 0 then return 0 end

        local id = buffer(current_index,1):string()
        fetch_subtree:add(buffer(current_index, 1), "Messege id: ", id)
        
        pinfo.cols.info = action .. " request: " .. id

    end
    

  end

  -- server

  if sender == "server" then
    
    -- OK
    if status == "ok" then
        current_index = 0
        
        current_index = incrementIndex(current_index, 4, buffer) -- skipping (ok/
        if current_index < 0 then return 0 end

        if buffer(current_index,1):string() == "\"" then
            local response_subtree = subtree:add(buffer(current_index, len-current_index-1), "Response details ") 
            
            current_index = incrementIndex(current_index, 1, buffer) --skipping first "  
            if current_index < 0 then return 0 end

            local messege = ""
            local loaded_bytes = 0
            
            messege, loaded_bytes = stringUntilQMarks(current_index, buffer)
            if loaded_bytes < 0 then return end

            current_index = incrementIndex(current_index, loaded_bytes, buffer)
            if current_index < 0 then return 0 end

            response_subtree:add(buffer(current_index-loaded_bytes, loaded_bytes), "Response messege: ", messege)

            if buffer(current_index+1,1):string() == ")" then
                pinfo.cols.info = "server response: " .. status .. " " .. messege

            else 
                -- user 
                
                current_index = incrementIndex(current_index, 3, buffer) --skipping " "
                if current_index < 0 then return 0 end

                local user = ""
                user, loaded_bytes = stringUntilQMarks(current_index, buffer)
                if loaded_bytes < 0 then return end
                
                current_index = incrementIndex(current_index, loaded_bytes, buffer)
                if current_index < 0 then return 0 end
                
                response_subtree:add(buffer(current_index-loaded_bytes, loaded_bytes), "Session token: ", user)
                pinfo.cols.info = "server response: " .. status .. " " .. messege .. ", session: " .. user
            end
        end
        
        -- fetch, list
        if buffer(current_index,1):string() == "(" then
            local response_subtree = subtree:add(buffer(current_index, len-current_index-1), "Response details ")
            
            current_index = incrementIndex(current_index, 1, buffer)
            if current_index < 0 then return 0 end

            if buffer(current_index,1):string() == "(" then
                local order = 1
                local messege_end = " "
                local id
                local loaded_bytes
                local block
                local name
                local list_pinfo = " "
                
                while messege_end == " " do
                    list_pinfo = list_pinfo .. "("
                    if order == 1 then
                        current_index = current_index +1 -- skipping ( 
                    else 
                        current_index = current_index +4
                    end

                    
                    block, loaded_bytes = stringUntilRBracket(current_index, buffer)
                    if loaded_bytes < 0 then return 0 end
                    
                    list_pinfo = list_pinfo .. block .. " "
                    local messege_end_index = current_index + loaded_bytes 
                    name = "Messege " ..  order
                    -- subparts of messege
                    local messege_subtree = response_subtree:add(buffer(current_index, loaded_bytes), name)
                    messege_subtree:add(buffer(current_index, loaded_bytes), "Raw data: ", block)
                    messege_subtree:add(buffer(current_index,1), "ID: ", buffer(current_index,1):string())
                    
                    current_index = incrementIndex(current_index, 3, buffer)
                    if current_index < 0 then return 0 end

                    local sender = ""
                    sender, loaded_bytes = stringUntilQMarks(current_index, buffer)
                    if loaded_bytes < 0 then return 0 end

                    current_index = incrementIndex(current_index, loaded_bytes, buffer)
                    if current_index < 0 then return 0 end
                    messege_subtree:add(buffer(current_index-loaded_bytes, loaded_bytes), "Sender: ", sender)

                    -- subject
                    current_index = incrementIndex(current_index, 3, buffer) --skipping " "
                    if current_index < 0 then return 0 end

                    local subject = ""
                    subject, loaded_bytes = stringUntilQMarks(current_index, buffer)
                    if loaded_bytes < 0 then return 0 end
                    
                    current_index = incrementIndex(current_index, loaded_bytes, buffer)
                    if current_index < 0 then return 0 end

                    messege_subtree:add(buffer(current_index-loaded_bytes, loaded_bytes), "Subject: ", subject)

                    messege_end = buffer(messege_end_index+1,1):string()
                    
                    order = order + 1

                    list_pinfo = list_pinfo .. ") "
                end 

                pinfo.cols.info = "server response: " .. status .. list_pinfo 

            
            -- empty list
            elseif buffer(current_index,1):string() == ")" then
                response_subtree:add(buffer(current_index-1, 2), "No messeges recieved")
                pinfo.cols.info = "server response: ok ()" 


            else
                -- fetch

                current_index = incrementIndex(current_index, 1, buffer)
                if current_index < 0 then return 0 end

                local sender = ""
                local loaded_bytes = 0
                sender, loaded_bytes = stringUntilQMarks(current_index, buffer)
                if loaded_bytes < 0 then return end
                
                current_index = incrementIndex(current_index, loaded_bytes, buffer)
                if current_index < 0 then return 0 end

                response_subtree:add(buffer(current_index-loaded_bytes, loaded_bytes), "Sender: ", sender)

                -- subject
                current_index = incrementIndex(current_index, 3, buffer) --skipping " "
                if current_index < 0 then return 0 end

                local subject = ""
                subject, loaded_bytes = stringUntilQMarks(current_index, buffer)
                if loaded_bytes < 0 then return end
                
                current_index = incrementIndex(current_index, loaded_bytes, buffer)
                if current_index < 0 then return 0 end
                
                response_subtree:add(buffer(current_index-loaded_bytes, loaded_bytes), "Subject: ", subject)

                -- messege
                current_index = incrementIndex(current_index, 3, buffer) --skipping " "
                if current_index < 0 then return 0 end

                local messege = ""
                messege, loaded_bytes = stringUntilQMarks(current_index, buffer)
                if loaded_bytes < 0 then return end
                
                current_index = incrementIndex(current_index, loaded_bytes, buffer)
                if current_index < 0 then return 0 end

                response_subtree:add(buffer(current_index-loaded_bytes, loaded_bytes), "Messege: ", messege)

                pinfo.cols.info = "server response: " .. status .. " (" .. sender .. " " .. subject .. " \"" .. messege .. "\")"     
            end
            
        end


    -- ERROR 
    elseif status == "err" then 
        current_index = 0
        
        current_index = incrementIndex(current_index, 5, buffer) -- skipping (err/
        if current_index < 0 then return 0 end

        local error_subtree = subtree:add(buffer(current_index, len-current_index-1), "Error details ") 
        
        current_index = incrementIndex(current_index, 1, buffer) --skipping first "  
        if current_index < 0 then return 0 end
        
        local error = ""
        local loaded_bytes = 0
        error, loaded_bytes = stringUntilQMarks(current_index, buffer)
        if loaded_bytes < 0 then return 0 end
        
        current_index = incrementIndex(current_index, 1, buffer)
        if current_index < 0 then return 0 end

        error_subtree:add(buffer(current_index-loaded_bytes, loaded_bytes), "Error messege: ", error)
        pinfo.cols.info = "server response: " .. status .. " " .. error
    end 

  end  

  
  return     
end


-- gets string until fist found right bracket (ignores brackets that are content of messege parts)
-- if right bracket not found, packet does not contain whole messege, another segment is added
function stringUntilRBracket(current_index, buffer)
    local loaded_bytes = 0
    local found_string = ""
    local current_byte 
    local ignoreQMark = false
    local insideString = false
    while true do 
        current_byte = buffer(current_index,1)
        if current_byte:string() == "\\" and ignoreQMark then
            ignoreQMark = false
        elseif current_byte:string() == "\\" then
            ignoreQMark = true
        elseif current_byte:string() == "\"" and ignoreQMark == false and insideString == false then
            insideString = true
        elseif current_byte:string() == "\"" and ignoreQMark == false and insideString == true then
            insideString = false
        elseif ignoreQMark then
            ignoreQMark = false
        elseif current_byte:string() == ")" and insideString == false then
            break;
        end
        found_string = found_string .. current_byte:string()
        loaded_bytes = loaded_bytes + 1
        current_index = incrementIndex(current_index, 1, buffer)
        if current_index < 0 then
            return found_string, -1
        end
    end
    return found_string, loaded_bytes
end


-- gets string until fist found question marks (ignores escaped question marks)
-- if question marks not found, packet does not contain whole messege, another segment is added
function stringUntilQMarks(current_index, buffer)
    local loaded_bytes = 0
    local found_string = ""
    local current_byte 
    local ignoreQMark = false
    while true do 
        current_byte = buffer(current_index,1)
        if current_byte:string() == "\\" and ignoreQMark then
            ignoreQMark = false
        elseif current_byte:string() == "\\" then
            ignoreQMark = true
        elseif current_byte:string() == "\"" and ignoreQMark == false then
            break;
        elseif ignoreQMark then
            ignoreQMark = false
        end
        found_string = found_string .. current_byte:string()
        loaded_bytes = loaded_bytes + 1
        current_index = current_index + 1
    end
    return found_string, loaded_bytes
end


-- increments index, if index out of range, packet does not contain whole messege
-- function then adds one more segment to process
function incrementIndex(current_index, amount, buffer)
    final_index = current_index + amount
    while current_index < final_index do
        current_index = current_index + 1
        if current_index > buffer:len() then
            pktinfo.desegment_len = DESEGMENT_ONE_MORE_SEGMENT
            pktinfo.desegment_offset = 0
            return -1
        end
    end
    return current_index
end

-- binding dissector to port 32323
local tcp_port = DissectorTable.get("tcp.port")
tcp_port:add(32323, isamail_protocol)


